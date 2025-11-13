import json
from src.Helper.GenerateGraficoHelper import GenerateGraficoHelper

class GraficoMetricaService:
    def __init__(self):
        self.metrics_file = 'metrics.json'
        self.nomes = []
        self.counts = []
        self.avg_score = []
        self.corrects = []
        self.wrongs = []

    def exibir_grafico(self):
        with open(self.metrics_file, "r", encoding="utf-8") as f:
            metrics = json.load(f)

        topics = metrics.get("topics", {})

        if not topics:
            print("Nenhum tópico encontrado para exibir.")
            return

        # Extrai dados corretamente
        self.nomes = list(topics.keys())
        self.counts = [t.get("count", 0) for t in topics.values()]
        self.avg_score = [t.get("avg_score", 0) for t in topics.values()]
        self.corrects = [t.get("correct", 0) for t in topics.values()]
        self.wrongs = [t.get("wrong", 0) for t in topics.values()]

        # Gráfico 1 - Contagem por tópico
        GenerateGraficoHelper.generateGrafico(
            x=self.nomes,
            y=self.counts,
            color="skyblue",
            title="Interações por Tópico",
            labelX="Tópico",
            labelY="Total",
            labelMain="Interações"
        )

        # Gráfico 2 - Score médio por tópico
        GenerateGraficoHelper.generateGrafico(
            x=self.nomes,
            y=self.avg_score,
            color="limegreen",
            title="Média de Score por Tópico",
            labelX="Tópico",
            labelY="Score Médio",
            labelMain="Score"
        )

        # Gráfico 3 - Correto x Errado
        GenerateGraficoHelper.generateGrafico(
            x=range(len(self.nomes)),
            y=self.corrects,
            color="green",
            labelMain="Corretos",

            extra=True,
            x_extra=range(len(self.nomes)),
            y_extra=self.wrongs,
            labelExtra="Errados",
            colorExtra="red",

            ticks=range(len(self.nomes)),
            ticks_labels=self.nomes,

            title="Corretos x Errados por Tópico",
            labelX="Tópico",
            labelY="Quantidade"
        )
