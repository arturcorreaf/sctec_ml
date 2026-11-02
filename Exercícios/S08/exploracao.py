import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path

pedidos = pd.read_csv("arquivos/pedidos2.csv")
produtos = pd.read_csv("arquivos/produtos2.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")   # dados brutos, sem limpeza

df["data"] = pd.to_datetime(df["data"])
nomes = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
df["dia"] = df["data"].dt.dayofweek.map(dict(enumerate(nomes)))
unicos = df.drop_duplicates()
bom = df[df["tempo_entrega_min"] < 120]

pasta = Path("arquivos/graficos")
pasta.mkdir(parents=True, exist_ok=True)
sns.set_theme(style="whitegrid")

# 1) Histograma do tempo de entrega, com os extremos
plt.figure(figsize=(5, 3.6))
sns.histplot(df["tempo_entrega_min"].dropna(), bins=20)
plt.title("Tempo de entrega (com extremos)")
plt.savefig(pasta / "tempo_com_extremos.png", dpi=120)
plt.close()
# O que vi: a maioria perto de 30 min, mas barras isoladas em 480: o eixo se estica e esmaga o que importa.
# O que faria: investigar os 480 min (parecem um código de erro) antes de usar a média.

# 2) Histograma abaixo de 120 minutos
plt.figure(figsize=(5, 3.6))
sns.histplot(bom["tempo_entrega_min"], bins=15)
plt.title("Tempo de entrega (abaixo de 120 min)")
plt.savefig(pasta / "tempo_sem_extremos.png", dpi=120)
plt.close()
# O que vi: sem as 3 entregas de 480 min o formato real aparece, entre 20 e 45 min, com cauda à direita.
# O que faria: registrar que o corte em 120 min é uma decisão minha.

# 3) Boxplot da quantidade por categoria
plt.figure(figsize=(5, 3.6))
sns.boxplot(data=df, x="categoria", y="qtd")
plt.title("Quantidade por categoria")
plt.savefig(pasta / "boxplot_qtd.png", dpi=120)
plt.close()
# O que vi: pedidos com 40 unidades em categorias diferentes, muito acima do resto.
# O que faria: perguntar ao negócio se são pedidos reais ou erro de digitação.

# 4) Pedidos por dia da semana (sem duplicados)
plt.figure(figsize=(5, 3.6))
sns.countplot(data=unicos, x="dia", order=nomes)
plt.title("Pedidos por dia da semana")
plt.savefig(pasta / "pedidos_por_dia.png", dpi=120)
plt.close()
# O que vi: sexta a domingo vendem cerca do dobro de segunda a quinta.
# O que faria: sugerir escala de equipe, estoque e promoções pensando no fim de semana.

print("Gráficos gravados em:", pasta)
for arquivo in sorted(pasta.glob("*.png")):
    print(" -", arquivo.name)
