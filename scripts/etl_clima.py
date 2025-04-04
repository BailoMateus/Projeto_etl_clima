import requests
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Função para buscar o clima atual de uma cidade
def buscar_clima(cidade):
    api_key = os.getenv("OWM_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados["main"]["temp"]
        umidade = dados["main"]["humidity"]
        descricao = dados["weather"][0]["description"]
        data_hora = datetime.now()

        return {
            "cidade": cidade,
            "temperatura": temperatura,
            "umidade": umidade,
            "descricao": descricao,
            "data_hora": data_hora
        }
    else:
        print("Erro ao acessar API:", resposta.status_code)
        return None


def salvar_no_banco(dados_clima):
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Clima (CIDADE, TEMPERATURA, UMIDADE, DATA_HORA)
        VALUES (%s, %s, %s, %s)
    """, (
        dados_clima["cidade"],
        dados_clima["temperatura"],
        dados_clima["umidade"],
        dados_clima["data_hora"]
    ))

    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Clima de {dados_clima['cidade']} salvo no banco com sucesso!")

# -------- EXECUÇÃO --------

cidades = ["Curitiba", "Londrina", "Foz do Iguaçu", "Guaratuba", "Itapoa", "São Paulo", "Rio de Janeiro"]

for cidade in cidades:
    clima = buscar_clima(cidade)
    if clima:
        salvar_no_banco(clima)
