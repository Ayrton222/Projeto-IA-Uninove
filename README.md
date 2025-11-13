# WeBot – Chatbot Inteligente de Help Desk (Projeto Acadêmico)

O **WeBot** é um chatbot de Help Desk desenvolvido para fins acadêmicos.
Ele coleta tópicos técnicos diretamente de um site, analisa perguntas do usuário e utiliza **IA generativa (Gemini)** para oferecer respostas mais amigáveis, claras e personalizadas.

O objetivo principal deste projeto é demonstrar:

* Coleta automática de tópicos/documentação na Web
* Similaridade semântica usando *Sentence Transformers*
* Interpretação da pergunta do usuário
* Geração de resposta via IA (Gemini)
* Registro de métricas e geração de gráficos analíticos
* Funcionamento de um chatbot real rodando em terminal

---

## Como o projeto funciona?

### 1. **Coleta de tópicos do site**

O serviço `ReadSiteDataService` acessa um site de documentação (definido no código) e extrai os tópicos e URLs de forma automática usando **BeautifulSoup**.

### 2. **Identificação do tópico mais relevante**

Quando o usuário faz uma pergunta, o projeto usa:

* Modelo **paraphrase-multilingual-MiniLM-L12-v2**
* Similaridade coseno

para identificar qual tópico possui maior relação semântica com a pergunta.

### 3. **Geração de resposta via IA**

Após identificar o melhor tópico:

* O texto técnico é extraído do site
* É enviado para o modelo **Gemini**
* O Gemini gera uma resposta mais natural, humana e prestativa

### 4. **Armazenamento de métricas**

Cada interação registra:

* Tópico encontrado
* Similaridade
* Se a resposta estava correta (feedback do usuário)

Os dados ficam em `metrics.json`.

### 5. **Geração de gráficos**

Ao encerrar, o sistema permite gerar 3 gráficos:

1. Interações por tópico
2. Score médio por tópico
3. Correto x Errado

Esses gráficos são exibidos usando **Matplotlib**.

---

##  Estrutura do Projeto

```
📦 projeto-chatbot
 ┣ 📂 src
 │  ┣ 📂 Config
 │  │  ┗ config.py
 │  ┣ 📂 DB
 │  │  ┗ metrics.json
 │  ┣ 📂 Helper
 │  │  ┗ GenerateGraficoHelper.py
 │  ┣ 📂 Service
 │  │  ┣ GraficoMetricaService.py
 │  │  ┣ MetricasService.py
 │  │  ┗ ReadSiteDataService.py
 │  ┗ main.py
 ┣ 📄 README.md
```

---

##  Chave API – Importante!

A chave **NÃO está incluída no código** por motivos de segurança.

Para adquirir sua **API KEY do Gemini**, consulte o **arquivo PDF enviado junto ao projeto**.

Inclua sua chave no arquivo:

```
src/Config/.env
```

com o conteúdo:

```
API_KEY=sua_chave_aqui
```

---

##  Instalação e Execução

###  1. Clone o projeto

```
git clone https://github.com/seu-repo/we-bot.git
cd we-bot
```

### 2. Crie um ambiente virtual (opcional, recomendado)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

###  3. Instale as dependências

```
pip install -r requirements.txt
```

###  4. Adicione sua API Key

Criar arquivo:

```
src/Config/.env
```

E colocar:

```
API_KEY=sua_chave
```

###  5. Execute o projeto

```
python main.py
```

---

## 🧾 Requisitos (requirements.txt)

```
google-generativeai
python-dotenv
requests
beautifulsoup4
sentence-transformers
torch
matplotlib
```
---

##  Objetivo Acadêmico

Este projeto demonstra:

* Aplicação prática de IA generativa
* Extração e classificação semântica de dados
* Integração de NLP com Web Scraping
* Persistência de métricas e visualização de dados
* Construção de um chatbot funcional no terminal

---

## Contribuições

Este é um projeto acadêmico, mas melhorias são bem-vindas:

* Nova camada de cache para web scraping
* Geração de relatórios automáticos
* Suporte a interface gráfica

---
## Responsáveis

= Ayrton Senna Cabani Bastos

Só pedir!
