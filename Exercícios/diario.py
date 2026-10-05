with open("arquivos/diario.txt", "a", encoding="utf-8") as diario:
  diario.write("Segunda entrada.\n")
  diario.write("Última entrada.\n")

entrada = input("Digite a entrada: ")
with open("arquivos/diario.txt", "a", encoding="utf-8") as diario:
  diario.write(entrada+"\n")

with open("arquivos/diario.txt","r", encoding="utf-8") as diario:
  for linha, texto in enumerate(diario):
    print(linha, texto)
