import pandas as pd 
vendas = pd.read_csv("Arquivos/vendas.csv")
vendas["total"] = vendas["quantidade"] * vendas["preco"]

resumo = vendas.groupby("categoria").agg(
    vendas=("total", "sum"),
    itens=("quantidade", "sum"),
    ticket=("preco","mean")
)

ranking = (vendas.groupby("categoria")["total"].sum().sort_values(ascending=False))

print("\nRESUMO DE VENDAS\n")
print(resumo)
print("\nRANKING DE CATEGORIAS\n")
print(ranking)

ranking.to_csv("Arquivos/resumo_categorias.csv")
print("\n--- Arquivos gravados com sucesso!---\n")