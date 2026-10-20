import numpy as np 

notas = np.array([[8.5, 9.0, 7.5],
                  [6.0, 7.5, 5.0],
                  [9.5, 8.0, 9.0],
                  [5.0, 6.0, 4.5]])
alunos = np.array(["Ana","Bruno","Carla","Diego"])

min = notas.min(axis=0) 
max = notas.max(axis=0)

minmax = (notas - min) / (max - min) 
print("\nMin-max por coluna:")
print(minmax.round(2))
print("\nMínimo de cada coluna:", minmax.min(axis=0), "| Máximo:", minmax.max(axis=0))

z = (notas - notas.mean(axis=0) / notas.std(axis=0))

print("\nZ-Score por coluna:")
print(z.round(2))
print("Média de cada coluna (perto de 0):", np.abs(z.mean(axis=0)).round(2))
print("Desvio-padrão de cada coluna (perto de 1):", z.std(axis=0).round(2))
