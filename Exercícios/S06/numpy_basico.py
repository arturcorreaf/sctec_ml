import numpy as np 

l = np.arange(1,13)
mat = l.reshape(3,4)
print(mat)
print("Shape:",mat.shape,"Dim:", mat.ndim, "Size:",mat.size)

# Segunda linha
print("Segunda linha:", mat[1, :])
# Última coluna
print("Última coluna:" , mat[:, -1])
# Bloco central
print("Bloco central:", mat[0:2, 1:3])
# Criar máscara de pares
mascara = mat % 2 == 0
# Colocando em lista
pares = mat[mascara]
# Contando 
qtd = np.sum(mascara)

print("Valores pares:", pares)
print("Quantidade de pares:", qtd)

