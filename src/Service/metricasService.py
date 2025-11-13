import os
import json
class MetricasService:
    def __init__(self,metrica_file = 'metrics.json'):
        self.metrica_file = metrica_file

    def load_metrics(self):
        if os.path.exists(self.metrica_file):
            with open(self.metrica_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"total_interactions": 0, "topics": {}}

    def save_metrics(self,metrics):
        with open(self.metrica_file, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=4, ensure_ascii=False)

    def update_metrics(self,topic, score, correct=None):
        metrics = self.load_metrics()
        metrics["total_interactions"] += 1

        topic_name = topic["titulo"]
        if topic_name not in metrics["topics"]:
            metrics["topics"][topic_name] = {"count": 0, "avg_score": 0, "correct": 0, "wrong": 0}

        t = metrics["topics"][topic_name]
        t["count"] += 1
        # Atualiza média de similaridade
        t["avg_score"] = ((t["avg_score"] * (t["count"] - 1)) + score) / t["count"]

        if correct is True:
            t["correct"] += 1
        elif correct is False:
            t["wrong"] += 1

        self.save_metrics(metrics)