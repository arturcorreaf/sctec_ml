import pandas as pd

pedidos = pd.read_csv("Arquivos/pedidos.csv")
clientes = pd.read_csv("Arquivos/clientes.csv")

# Merge left
esq = pedidos.merge(clientes, on="id_cliente", how="left")
print(esq[["id_pedido", "nome" , "valor"]])

# Preencher ausentes
esq["nome"] = esq["nome"].fillna("Cliente não cadastrado")
esq["cidade"] = esq["cidade"].fillna("Sem Cidade")
print(esq[["id_pedido", "nome" , "valor"]])

# Categorizar Valor

esq["faixa"] = "Baixo"
esq.loc[esq["valor"] > 500, "faixa"] = "Alto"

# Resumo
total_cidade = esq.groupby("cidade")["valor"].sum()
produto_cidade = esq.pivot_table(index="produto", columns="cidade",
                                  values="valor", aggfunc="sum", fill_value=0)

total_cidade.to_csv("Arquivos/total_por_cidade.csv")
produto_cidade.to_csv("Arquivos/produto_por_cidade.csv")

print(esq[["id_pedido", "nome", "valor", "faixa"]])
print("\nTotal por cidade:")
print(total_cidade)
print("\nProduto por cidade:")
print(produto_cidade)