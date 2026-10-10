from datetime import datetime
import re

def limpar_nome(nome):
    """Tira espaços extras e padroniza a caixa."""
    return " ".join(nome.split()).title()

def limpar_fone(fone):
    """Remove tudo que não é número."""
    return re.sub(r"\D", "", fone)

def fone_valido(fone):
    """Valida o telefone (11 dígitos)"""
    return re.fullmatch(r"\d{11}", fone) is not None

def limpar_data(texto):
    """Formata a data para AAAA-MM-DD."""
    return datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d")

if __name__ == "__main__":
    assert limpar_nome("  Marcos FELIPE ") == "Marcos Felipe"
    assert limpar_fone("(48)91234-4567") == "48912344567"
    assert limpar_data("05/03/2025") == "2025-03-05"
    assert fone_valido("48912344567") is True
    assert fone_valido("489999999") is False
    print("Testes ok!")