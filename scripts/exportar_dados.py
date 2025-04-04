import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()


conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

query = """
    SELECT 
           ID
          ,CIDADE
          ,TEMPERATURA
          ,UMIDADE
          ,DATA_HORA
    FROM clima   
"""

df = pd.read_sql(query, conexao)

df.to_csv("../data/dados_clima.csv", index=False, encoding='utf-8')

print("Dados Exportados com Sucesso para dados_clima.csv!")

conexao.close