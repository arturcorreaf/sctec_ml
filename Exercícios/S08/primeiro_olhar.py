import pandas as pd

pedidos = pd.read_csv("arquivos/pedidos2.csv")
produtos = pd.read_csv("arquivos/produtos2.csv")
df = pedidos.merge(produtos, on="id_produto", how="left")   # dados brutos, sem limpeza

print("Tamanho:", df.shape)

# head transposto: todas as colunas de uma vez
print(df.head(3).T)

# Tipos e contagem de não nulos
df.info(memory_usage=False)

colunas = ["qtd", "avaliacao", "tempo_entrega_min", "preco"]
print(df[colunas].describe().round(1))

# Ausentes: quantidade e proporção
tabela = pd.DataFrame({"nulos": df.isna().sum(), "pct": (df.isna().mean() * 100).round(1)})
print(tabela[tabela["nulos"] > 0])

# Duplicados
print(df.duplicated().sum(), "linhas duplicadas |", df.duplicated(subset="id_pedido").sum(), "ids repetidos")

# Categorias
print(df["canal"].nunique(), "variações de canal")
print(df["canal"].value_counts())

# Observações:
# 1) data está como texto (str), não como data.
# 2) qtd tem mínimo -1 (impossível) e máximo 40 (muito acima da mediana de 1).
# 3) tempo_entrega_min tem máximo 480, bem acima da mediana, e 82,7% de ausentes.
