from datetime import datetime
import re, csv

padrao= r"\d{11}"

with open("arquivos/sujo.csv", newline="", encoding="utf-8") as f:
  for contato in csv.DictReader(f):
    nome = re.sub(r"\s+", " ", contato["nome"]).strip().title()
    fone = re.sub(r"\D", "", contato["telefone"])
    data = datetime.strptime(contato["data"], "%d/%m/%Y")
    print(nome,fone,data.strftime("%d/%m/%Y"),end="\n")

with open("arquivos/limpo.csv","w", newline="", encoding="utf-8") as l:
    escritor = csv.DictWriter(l, fieldnames=["nome","telefone","data"])
    escritor.writeheader()
    for contato in csv.DictReader(f):
        escritor.writerow({
            "nome": nome,
            "telefone": fone,
            "data": data.strftime("%d/%m/%Y")
        })