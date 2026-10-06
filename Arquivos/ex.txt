import csv

with open("notas.csv", newline="", encoding="utf-8") as notas:
  with open("resultado.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nome", "media", "situacao"])
    escritor.writeheader()                           
    for aluno in csv.DictReader(notas):
        media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
        if media >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"{aluno['nome']} - {situacao} - Média: {media:.2f}")
        
        escritor.writerow({"nome": aluno["nome"], "media": round(media, 2), "situacao": situacao})
import csv
 
with open("notas.csv", newline="", encoding="utf-8") as arquivo:
    alunos = list(csv.DictReader(arquivo))
 
resultado = []
for aluno in alunos:

    media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
 
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
 
    resultado.append({
        "nome": aluno["nome"],
        "media": round(media, 2),
        "situacao": situacao,
    })

with open("resultado.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "media", "situacao"])
    escritor.writeheader()
    escritor.writerows(resultado)
 
print("resultado.csv gravado com", len(resultado), "alunos")