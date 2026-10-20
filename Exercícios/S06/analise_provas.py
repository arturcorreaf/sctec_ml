import pandas as pd
import numpy as np
import time

# Leitura do pandas e matriz ao numpy.
df = pd.read_csv("arquivos/provas.csv")
notas = df[["p1","p2","p3"]].to_numpy()

# Faz a média ponderada via broadcasting, arredonda com 2 casas decimais, e classifica a situação.
pesos = np.array([0.3, 0.3, 0.4])
df["final"] = (notas * pesos). sum(axis=1).round(2) 
df["situacao"] = np.where(df[ "final"] >= 7, "Aprovado", "Reprovado") 
print("\n====== Notas Finais =====\n")
print(df[["nome", "final", "situacao"]])

# Z-scores
z = (notas - notas.mean(axis=0) / notas.std(axis=0))
df["z_p1"] = z[:, 0].round(2)
df["z_p2"] = z[:, 1].round(2)
df["z_p3"] = z[:, 2].round(2)

print("\n======== Z-Scores =======\n")
print(df[["nome","p1","z_p1","p2","z_p2","p3","z_p3"]])

print("\nGravando relatório...")
time.sleep(3) # Tempo de espera para o arquivo ser salvo. (Apenas "estético")

## Salvando o dataframe no arquivo.
df.to_csv("arquivos/resultado_provas.csv", index=False)
print("Relatório criado com sucesso: resultado_provas.csv\n")


