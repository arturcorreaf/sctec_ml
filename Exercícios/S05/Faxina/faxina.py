import csv
import limpeza

with open("arquivos/sujo.csv", newline="", encoding="utf-8") as f, \
     open("arquivos/limpo.csv", "w", newline="", encoding="utf-8") as l:

    leitor = csv.DictReader(f)
    escritor = csv.DictWriter(
        l,
        fieldnames=["nome", "telefone", "data"]
    )

    escritor.writeheader()

    for contato in leitor:
        nome = limpeza.limpar_nome(contato["nome"])
        fone = limpeza.limpar_fone(contato["telefone"])
        data = limpeza.limpar_data(contato["data"])

        escritor.writerow({
            "nome": nome,
            "telefone": fone,
            "data": data
        })

        print(nome, fone, data)