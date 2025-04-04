import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df = pd.read_csv("../data/dados_clima.csv")
df["DATA_HORA"] = pd.to_datetime(df["DATA_HORA"])

plt.style.use("seaborn-v0_8-dark")

fig, ax = plt.subplots(figsize=(12, 6))

for cidade in df["CIDADE"].unique():
    dados_cidade = df[df["CIDADE"] == cidade]
    ax.plot(dados_cidade["DATA_HORA"], dados_cidade["TEMPERATURA"], marker="o", label=cidade)

ax.set_title("Variação de Temperatura por Cidade", fontsize=16, weight='bold')
ax.set_xlabel("Data e Hora", fontsize=12)
ax.set_ylabel("Temperatura (°C)", fontsize=12)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %Hh'))
plt.xticks(rotation=45)
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(title="Cidade")

plt.tight_layout()
plt.savefig("../images/grafico_temperatura_media.png")
plt.show()

# ----------- Gráfico 2: Variação de Umidade por Cidade -----------
fig, ax = plt.subplots(figsize=(12, 6))

for cidade in df["CIDADE"].unique():
    dados_cidade = df[df["CIDADE"] == cidade]
    ax.plot(dados_cidade["DATA_HORA"], dados_cidade["UMIDADE"], marker="s", label=cidade)

ax.set_title("Variação de Umidade por Cidade", fontsize=16, weight='bold')
ax.set_xlabel("Data e Hora", fontsize=12)
ax.set_ylabel("Umidade (%)", fontsize=12)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %Hh'))
plt.xticks(rotation=45)
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(title="Cidade")

plt.tight_layout()
plt.savefig("../images/grafico_variacao_temperatura.png")
plt.show()
