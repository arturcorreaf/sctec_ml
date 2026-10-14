alunos = [
           {"nome": "Ana", "nota": 9.0}, 
           {"nome": "Carlos", "nota": 6.5},
           {"nome": "Clara", "nota": 8.0}, 
           {"nome": "Luis", "nota": 5.0},
           {"nome": "Pedro", "nota": 7.0}
          ]

# Ordena do maior para o menor pela nota
por_nota = sorted(alunos, key=lambda a: a["nota"], reverse=True)
print("Alunos ordenados: \n")
for a in por_nota:
    print(a["nome"], "|", a["nota"])

# filtra só quem tem nota >= 7
aprovados = list(filter(lambda a: a["nota"] >= 7, alunos))
print("\nAprovados: ", [a["nome"] for a in aprovados])

