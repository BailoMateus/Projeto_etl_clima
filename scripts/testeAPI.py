import requests
import os
from dotenv import load_dotenv

load_dotenv()

print("API KEY:", os.getenv("OWM_API_KEY"))

api_key = os.getenv("OWM_API_KEY")
cidade = "Curitiba"
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados["main"]["temp"]
    umidade = dados["main"]["humidity"]
    descricao = dados["weather"][0]["description"]

    print(f"Clima em {cidade}: {descricao}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade: {umidade}%")
else:
    print("Erro ao acessar a API:", resposta.status_code)
