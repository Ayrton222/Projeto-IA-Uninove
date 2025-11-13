from src.Config.config import Config
from src.Service.metricasService import MetricasService
from src.Service.readSiteDataService import ReadSiteDataService
from src.Service.GraficoMetricaService import GraficoMetricaService
import re

def generate_ai_response(ai_config, conversation_history, user_input, article_text=None):

    history_text = "\n".join([f"Usuário: {u}\nAssistente: {a}" for u, a in conversation_history])
    doc_context = f"\nBaseie-se neste conteúdo técnico:\n{article_text}" if article_text else ""

    prompt = f"""
{ai_config.get_persona()}

Histórico da conversa:
{history_text}
    
Usuário perguntou: "{user_input}"
{doc_context}

Responda de forma natural, breve e prestativa.
"""
    model = ai_config.get_model()
    response = model.generate_content(prompt)
    return response.text.strip()


def main():
    print("Olá! Eu sou o *WeBot*, assistente da Agência We Digital, especializado em CRM.")
    print("Posso te ajudar a entender nossas soluções, tirar dúvidas técnicas ou te orientar sobre o CRM.")
    print("Digite 'sair' para encerrar.\n")

    ai_config = Config()
    metricas = MetricasService(metrica_file="src/DB/metrics.json")
    site_data = ReadSiteDataService()

    site_data.get_topics()
    if not site_data.topics:
        print("Nenhum tópico encontrado na documentação.")
        return

    conversation_history = []

    grafico_service = GraficoMetricaService()

    while True:
        user_input = input("Você: ").strip()

        if user_input.lower() in ["sair", "exit", "tchau"]:

            print("\nTem certeza que deseja sair?")
            print("1 - Sim, desejo sair")
            print("2 - Não, quero visualizar os resultados primeiro")
            print("3 - Cancelar")

            escolha = input("Escolha uma opção: ").strip()

            if escolha == "1":
                print("👋 Até mais! Foi um prazer te ajudar.")
                break

            elif escolha == "2":
                print("\nGerando gráficos de métricas...\n")
                grafico_service.exibir_grafico()
                print("\nAté mais! Foi um prazer te ajudar.")
                break

            else:
                print("Operação cancelada. Vamos continuar!\n")
                continue
        best_topic, score = site_data.find_best_topic(user_input)
        print(f"Tópico mais relevante: {best_topic['titulo']} (Score: {score:.2f})")

        article_text = site_data.extract_article_text() if score > 0.4 else ""

        ai_response = generate_ai_response(ai_config, conversation_history, user_input, article_text)
        print(f"WeBot: {ai_response}\n")

        correct_input = input("A resposta foi correta? (s/n): ").strip().lower()
        correct = True if correct_input == "s" else False if correct_input == "n" else None
        metricas.update_metrics(best_topic, score, correct)

        conversation_history.append((user_input, ai_response))


if __name__ == "__main__":
    main()
