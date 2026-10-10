def e_bissexto(ano):
    """Retorna True se o ano for bissexto."""
    if ano % 4 != 0:
        return False
    elif ano % 100 == 0 and ano % 400 != 0:
        return False
    else:
        return True

def calcular_imc(peso,altura):
    """Calcula o IMC, devolvendo um valor inteiro"""
    return peso//(altura**2)

help(e_bissexto)
print(e_bissexto(2004), e_bissexto(1900), e_bissexto(2024), e_bissexto(2023))
help(calcular_imc)
print(calcular_imc(100,1.85))
print(calcular_imc(80,1.75))

