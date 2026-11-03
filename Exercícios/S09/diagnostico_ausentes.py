import pandas as pd
import numpy as np

# Lendo o bd e checando shape e colunas
bruto = pd.read_csv("arquivos/imoveis_bruto.csv")
print("shape:", bruto.shape)
print("colunas de texto:", bruto.select_dtypes(exclude="number").columns.tolist())

# Checando os valores disfarçados
print(bruto["area_m2"].dtype)
print(bruto["condicao"].value_counts(dropna=False).tail(4))
print(bruto["idade_anos"].min())
print(bruto["area_m2"][pd.to_numeric(bruto["area_m2"], errors="coerce").isna()].value_counts())


# Relendo arquivo e dando replace
imoveis = pd.read_csv("arquivos/imoveis_bruto.csv", na_values=["N/D", "?", "s/i"])
imoveis["idade_anos"] = imoveis["idade_anos"].replace(-1, np.nan)
ausentes = imoveis.isna().sum()
print(ausentes[ausentes > 0])
print((imoveis["idade_anos"].isna().groupby(imoveis["tipo"]).mean() * 100).round(1))
