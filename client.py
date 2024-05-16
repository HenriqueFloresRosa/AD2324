import requests
import json

class Cliente:
    def __init__(self, servidor_url):
        self.servidor_url = servidor_url

    def criar_pergunta(self, questions, answers, k):
        dados = {
            "operacao": "QUESTION",
            "texto_pergunta": questions,
            "opcoes": answers,
            "opcao_correta": k
        }
        resposta = requests.post(self.servidor_url, json=dados)
        return resposta.text

    def obter_pergunta(self, id_pergunta):
        dados = {
            "operacao": "QUESTIONGET",
            "id_pergunta": id_pergunta
        }
        resposta = requests.post(self.servidor_url, json=dados)
        return resposta.json()

    

# Exemplo de uso:
cliente = Cliente("http://localhost:8000")  # Substituir pela URL do servidor
resposta = cliente.criar_pergunta("Qual é a capital do Brasil?", ["Rio de Janeiro", "São Paulo", "Brasília"], 2)
print(resposta)

resposta = cliente.obter_pergunta(1)
print(resposta)
