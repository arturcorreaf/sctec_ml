import time
import pandas as pd 

df = pd.read_csv("Arquivos/vendas.csv")

df["total"] = df["quantidade"] * df["preco"] # Criando coluna Total.
media = df["total"].mean() # Calcula a média dos valores totais.
acima_media = df.loc[df["total"] > media] # Calcula as vendas acima da média.

print("\n === Relatório de Vendas ===")
print("\nValor médio do total: R$",media)
print("Vendas acima da média:", len(acima_media))
print("Tipo de produto mais vendido:", df["categoria"].value_counts().idxmax())


print ("\n\nSalvando relatório...")
acima_media.to_csv("Arquivos/maiores_que_a_media.csv", index=False) # Salvando o arquivo, apenas as vendas acima da média. 
time.sleep(2) # Tempo de espera para o arquivo ser salvo. (Apenas "estético")
print("Arquivo gravado com sucesso!\n")
