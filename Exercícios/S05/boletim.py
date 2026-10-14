import csv

with open("arquivos/notas.csv", newline="", encoding="utf-8") as notas:
  leitor = csv.reader(notas)
  for linha in leitor:
    print(linha)

with open("arquivos/notas.csv", newline="", encoding="utf-8") as notas:

  with open("arquivos/resultado.csv","w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=["nome","media", "situacao"])

    escritor.writeheader()

    for aluno in csv.DictReader(notas):
      media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
      if media>= 7:
        print(f"{aluno['nome']} - Aprovado - Média: {media:.2f}")
        situacao = "Aprovado"
      else:
        print(f"{aluno['nome']} - Reprovado - Média: {media:.2f}")
        situacao = "Reprovado"

      escritor.writerow({
        "nome": aluno["nome"], 
        "media": round(media, 2), 
        "situacao": situacao})


