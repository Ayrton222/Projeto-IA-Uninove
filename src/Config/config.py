import os
import google.generativeai as genai
from dotenv import load_dotenv

class Config:

    def __init__(self, model_name='models/gemini-2.5-pro',temperature=0.7):
        env_path = os.path.join(os.path.dirname(__file__), ".env")
        load_dotenv(dotenv_path=env_path)

        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API_KEY not found")
        genai.configure(api_key=self.api_key)
        self.model_name = model_name
        self.temperature = temperature
        self.model = genai.GenerativeModel(self.model_name)

        self.persona = f"""
            Você é o assistente virtual da Agência We Digital, especializado em CRM e soluções digitais.
            Seu nome é **WeBot**, e você fala de forma simpática e profissional.
            Se o usuário fizer perguntas sobre a agência, apresente-se.
            Se a pergunta for sobre outros temas, ajude brevemente e redirecione para o CRM.
            Se não souber algo, seja honesto e oriente o usuário a buscar suporte humano.
            Responda de forma natural, breve e prestativa.
        """

    def get_model(self):
        return self.model

    def get_temperature(self):
        return self.temperature

    def get_persona(self):
        return self.persona