import pandas as pd 

pedidos = pd.read_csv('arquivos/pedidos2.csv')

print(f'Shape: {pedidos.shape}')

# Criar colunas mes e dia da semana
pedidos["data"] = pd.to_datetime(pedidos["data"])
pedidos["mes"] = pedidos["data"].dt.month
pedidos["dia_semana"] = pedidos["data"].dt.dayofweek
print(pedidos[["data", "mes", "dia_semana"]].head(3))

# Padronizando canais
print(pedidos["canal"].value_counts())
pedidos["canal"] = pedidos["canal"].str.strip().str.title()
print(pedidos["canal"].value_counts())

dias = {0: "segunda", 1: "terça", 2: "quarta", 3: "quinta", 4: "sexta", 5: "sábado", 6: "domingo"}
pedidos["dia_semana"] = pedidos["dia_semana"].map(dias)
print(pedidos[["data", "dia_semana"]].head(3))

# Função para faixa tempo
def faixa_tempo(minutos):
    if pd.isna(minutos):
        return "sem entrega"
    if minutos <= 30:
        return "rapida"
    return "demorada"

# Usando apply para criar faixa de entrega
pedidos["faixa_entrega"] = pedidos["tempo_entrega_min"].apply(faixa_tempo)
print(pedidos[["faixa_entrega"]].value_counts())