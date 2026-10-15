import pandas as pd 

sujo = pd.read_csv("arquivos/contatos_sujos.csv")
sujo = sujo.drop_duplicates()
media = sujo["nota"].mean()
sujo["nota"] = sujo["nota"].fillna(media)
sujo["nome"] = (sujo["nome"].str.strip().str.replace(r"\s+", " ", regex=True).str.title())
sujo["telefone"] = (sujo["telefone"].str.replace(r"\D", "", regex=True))
sujo["data_cadastro"] = pd.to_datetime(sujo["data_cadastro"], format="%d/%m/%Y")

print(sujo[["nome", "telefone", "nota", "data_cadastro"]])
print("\nMédia de notas: ",round(media,2))

sujo[["nome", "telefone", "nota", "data_cadastro"]].to_csv("Arquivos/contatos_limpos.csv", index=False) # Exportando apenas os dados de vendas acima de 1000.
print("\n--- Arquivo gravado com sucesso!---\n")

