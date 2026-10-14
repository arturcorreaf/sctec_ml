contatos = []

def adicionar(nome, telefone):
    contatos.append({"nome": nome, "telefone": telefone})
    print(f"{nome} foi adicionado à agenda. \n")

def buscar(nome):
    for contato in contatos:
        if contato["nome"] == nome:
            return contato["telefone"]
    return None

def listar():
    print("Lista de contatos:")
    for contato in contatos:
        print(contato["nome"], "- ", contato["telefone"])

adicionar("Clara", "48 9999-0001")
adicionar("Jorge", "48 9999-0002")
adicionar("Patricia", "48 9999-0003")
adicionar ("Sofia", "48 9999-0004")
adicionar ("Thiago", "48 9999-0005")
adicionar("Daniel", "48 9999-0006")
adicionar("Julia", "48 9999-0007")

opcao=""

while opcao!=0:
  opcao = int(input(
    "=== AGENDA TELEFÔNICA ===\n\n"
    "1 - Adicionar contato\n"
    "2 - Buscar contato\n"
    "3 - Listar contatos\n"
    "0 - Sair\n\n"
    "Escolha uma opção: "))
    
  if opcao == 1:
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    adicionar(nome, telefone)
  elif opcao == 2:
    nome = input("Digite o nome: ")
    if buscar(nome):
      print("Telefone:",buscar(nome),"\n")
    else:
      print("Não encontrado.\n")
  elif opcao == 3:
    listar()
    
print("Saindo...")
