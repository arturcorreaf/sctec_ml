import pandas as pd 

df = pd.read_csv("Arquivos/vendas.csv")
print("Linhas e colunas:", df.shape)
print("\nColunas:\n", df.columns)
print("\nTipos de dados: \n", df.dtypes)
print("\nDescrição: \n",df.describe())
print("\n################################\n")

df["total"] = df["quantidade"] * df["preco"]
caros = df.loc[df["total"] > 1000]
print("\nVendas acima de R$ 1.000:\n\n",caros)
print("\nVendas de Florianópolis ou Blumenau:\n\n",df[(df["cidade"] == "Florianópolis") | (df["cidade"] == "Blumenau")])
print("\nProduto mais caro:",df.loc[df["preco"].idxmax()]["produto"])

caros.to_csv("Arquivos/relatorio_caros.csv", index=False) # Exportando apenas os dados de vendas acima de 1000.
print("\n--- Arquivo gravado com sucesso!---\n")