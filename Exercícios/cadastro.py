pessoa={"Nome": "Paulo", "Idade": 30, "Cidade": "Criciúma", "Profissão": "Advogado"}
print(pessoa)
pessoa.update({"E-mail": "paulo@gmail.com"})
print(pessoa)

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

