import re, csv

padrao = r"\d{11}"

with open("arquivos/contatos.csv", newline="", encoding="utf-8") as f:
  for contato in csv.DictReader(f):
    original = contato["telefone"]
    limpo = re.sub(r"\D", "", original)
    valido = re.fullmatch(padrao, limpo)
    situacao = "válido" if valido else "inválido"
    print("O número", original,"de",contato["nome"],"é",situacao)


