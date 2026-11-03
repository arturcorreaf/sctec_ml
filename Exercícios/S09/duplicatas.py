import pandas as pd
import numpy as np

imoveis = pd.read_csv("arquivos/imoveis_bruto.csv", na_values=["N/D", "?", "s/i"])
print("Linhas duplicadas (todas as colunas):", imoveis.duplicated().sum())
print("Bairros distintos antes:", imoveis["bairro"].nunique())

imoveis["bairro"] = imoveis["bairro"].str.strip().str.title()
print("Bairros distintos depois:", imoveis["bairro"].nunique())

colunas = [c for c in imoveis.columns if c != "id_anuncio"]
print("Duplicadas (sem o id):", imoveis.duplicated(subset=colunas).sum())
sem_dup = imoveis.drop_duplicates(subset=colunas)
print("Total de linhas restantes:", len(imoveis), "->", len(sem_dup))
