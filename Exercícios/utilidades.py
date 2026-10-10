def media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas)//len(notas)

def desconto(preco, percentual=10):
    """Calcula o valor do desconto."""
    return preco-(preco*(percentual/100))

def estatisticas(stats):
    """Calcula estatísticas das notas (Máximo, mínimo e média)"""
    return min(stats), max(stats), media(stats)
    
def situacao(media):
    """Calcula a situacao do aluno"""
    if media>=7:
        return "Aprovado"
    return "Reprovado"

print(help(estatisticas))
print(help(situacao))
print(help(media))
print(help(desconto))

# Argumentos posicionais e nomeados
print("Média:", round(media([10,8,7]), 1))
print("Desconto padrão (10%):", desconto(500))
print ("Desconto de 25% (posicional):", desconto(200,25))
print ("Desconto de 25% (nomeado):", desconto(percentual=25, preco=200))

# Retorno múltiplo
minimo, maximo, media = estatisticas([1,2,3,4,5,6,7,8,9,10])
print ("Mínimo:", minimo, "| Máximo:", maximo, "| Média: ", media)

# situacao() dentro de um for

for nota in [8.5, 6.0, 7.0, 4.5]:
    print("Média", nota, "->", situacao(nota))
