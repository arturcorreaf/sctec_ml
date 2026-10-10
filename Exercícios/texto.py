import re
from datetime import datetime

def so_digitos(texto):
    return re.sub(r"\D", "", texto)

def normalizar_nome(nome):
    return " ".join(nome.split()).title()

def formatar_data(texto):
    return datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d")        

if __name__ == "__main__":
    print("Teste de funções")
    print(f"Telefone: {so_digitos('(48) 99123-1122')}")
    print(f"Nome: {normalizar_nome('Ana  CLARA  ')}")
    print(f"Data: {formatar_data("05/04/2025")}")