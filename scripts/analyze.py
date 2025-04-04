import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../data/dados_clima.csv")

df["DATA_HORA"] = pd.to_datetime(df["DATA_HORA"])


df = df.sort_values(by="DATA_HORA")

# ----------- Gráfico 1: Temperatura média por cidade -----------
plt.figure(figsize=(10, 6))
df.groupby("CIDADE")["TEMPERATURA"].mean().plot(kind="bar", color="skyblue")
plt.title("Temperatura Média por Cidade")
plt.ylabel("Temperatura (°C)")
plt.xlabel("Cidade")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/grafico_temperatura_media.png")
plt.show()

# ----------- Gráfico 2: Variação de temperatura ao longo do tempo por cidade -----------
plt.figure(figsize=(12, 6))
for cidade in df["CIDADE"].unique():
    cidade_df = df[df["CIDADE"] == cidade]
    plt.plot(cidade_df["DATA_HORA"], cidade_df["TEMPERATURA"], label=cidade)

plt.title("Variação de Temperatura ao Longo do Tempo")
plt.ylabel("Temperatura (°C)")
plt.xlabel("Data e Hora")
plt.legend()
plt.tight_layout()
plt.savefig("../images/grafico_variacao_temperatura.png")
plt.show()
