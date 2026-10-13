import pandas as pd 

notas = pd.Series([7.5, 5.0, 3.5, 9.0], index=["Clara", "Emmanuel", "Lia", "Mariana"])

print("Média da turma: ",notas.median())
print("Aluno com a maior nota: ", notas.idxmax(),"|", notas.max())
print("")

filmes = {
    "titulo": ["Lord of the Rings: The Return of the King", "Project Hail Mary", "Obsession"],
    "ano": [2003, 2026, 2025],
    "nota": [9.0, 8.2, 7.8],
    }

mini = pd.DataFrame(filmes)
print(mini["titulo"])
print(mini[["ano","nota"]])
print(mini.dtypes[["ano","nota"]])