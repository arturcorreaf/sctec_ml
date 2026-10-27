import pandas as pd 
import numpy as np

pedidos = pd.read_csv('arquivos/pedidos2.csv')

# Criar colunas mes e dia da semana
pedidos["data"] = pd.to_datetime(pedidos["data"])
pedidos["mes"] = pedidos["data"].dt.month
pedidos["dia_semana"] = pedidos["data"].dt.dayofweek
print(pedidos[["data", "mes", "dia_semana"]].head(3))

# Padronizando canais
print(pedidos["canal"].value_counts())
pedidos["canal"] = pedidos["canal"].str.strip().str.title()
print(pedidos["canal"].value_counts())

# Nomeando dias da semana
dias = {0: "segunda", 1: "terça", 2: "quarta", 3: "quinta", 4: "sexta", 5: "sábado", 6: "domingo"}
pedidos["dia_semana"] = pedidos["dia_semana"].map(dias)
print(pedidos[["data", "dia_semana"]].head(3))

# Determinando pedidos grandes
pedidos["pedido_grande"] = np.where(
    pedidos["qtd"] >= 3, 
    "sim",
    "nao"
)
print(pedidos["pedido_grande"].value_counts())

condicoes = [
    pedidos["avaliacao"] >= 4,
    pedidos["avaliacao"] == 3,
    pedidos["avaliacao"] <= 2,
]

rotulos =  ["satisfeito", "neutro", "insatisfeito"]

pedidos['perfil'] = np.select(condicoes, rotulos, default="sem nota")
print(pedidos["perfil"].value_counts())

pedidos["taxa_entrega"] = 0.0
pedidos.loc[pedidos["canal"] == "Delivery", "taxa_entrega"] = 4.5
print(pedidos.groupby("canal")["taxa_entrega"].agg(["min", "max"]))

faixas = pd.cut(
    pedidos["tempo_entrega_min"],
    bins=[0,20,30,45, np.inf],
    labels=["ate 20","21-30","31-45","mais de 45"],
)

print(faixas.value_counts().sort_index())