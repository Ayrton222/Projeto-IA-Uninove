import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
import torch
import re

class ReadSiteDataService:

    def __init__(self, url = 'https://agenciawedigital.com.br/docs/'):
        self.url = url
        self.topics = ''

    def get_url(self):
        return self.url

    def get_topics(self):
        print("🔎 Buscando tópicos do site...")
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, "html.parser")

        topics = []
        for section in soup.select("div.x-col.e2607-e8"):
            section_title_tag = section.select_one("h1.x-text-content-text-primary")
            if not section_title_tag:
                continue
            section_title = section_title_tag.get_text(strip=True)

            for link in section.select("a.x-text"):
                title_tag = link.select_one("h1.x-text-content-text-primary")
                if not title_tag:
                    continue
                topic_title = title_tag.get_text(strip=True)
                topic_url = link.get("href")

                topics.append({
                    "categoria": section_title,
                    "titulo": topic_title,
                    "url": topic_url
                })

        print(f"✅ {len(topics)} tópicos encontrados.")
        self.topics =  topics

    def find_best_topic(self,user_input):
        model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        titles = [t["titulo"] for t in self.topics]
        embeddings = model.encode(titles, convert_to_tensor=True)
        input_emb = model.encode(user_input, convert_to_tensor=True)

        sim = util.cos_sim(input_emb, embeddings)[0]
        best_score, idx = torch.max(sim, dim=0)
        return self.topics[idx], float(best_score)

    def extract_article_text(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, "html.parser")

        content_divs = soup.select("div.x-text.x-content")
        paragraphs = []
        for div in content_divs:
            for img in div.find_all("img"):
                img.decompose()
            text = div.get_text(separator=" ", strip=True)
            text = re.sub(r"\s+", " ", text)
            if text:
                paragraphs.append(text)
        return " ".join(paragraphs) if paragraphs else ""
