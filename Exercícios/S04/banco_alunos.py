alunos = [
    {"nome": "Clara", "nota": 9.2},
    {"nome": "Rafael", "nota": 5.5},
    {"nome": "Davi", "nota": 8.4},
    {"nome": "Helena", "nota": 7.1},
    {"nome": "Sofia", "nota": 4.5},
    {"nome": "Miguel", "nota": 9.0},
]

qtd = 0

for aluno in alunos:
    if aluno["nota"] >= 7:
        qtd+=1
        print(aluno["nome"], "aprovado(a).")

print("Foram aprovados", qtd, "alunos.")
