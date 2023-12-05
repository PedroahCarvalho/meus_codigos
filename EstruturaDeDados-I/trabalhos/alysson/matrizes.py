import numpy as np
from tabulate import tabulate

def melhor_volta(matriz_tempos, corredores):
    melhor_tempo = float('inf')
    melhor_corredor = ""
    volta_melhor_tempo = 0

    for corredor in corredores:
        tempos_corredor = matriz_tempos[corredor - 1]
        for volta, tempo in enumerate(tempos_corredor, start=1):
            if tempo < melhor_tempo:
                melhor_tempo = tempo
                melhor_corredor = f"Corredor {corredor}"
                volta_melhor_tempo = volta

    return melhor_corredor, volta_melhor_tempo

def classificacao_final(matriz_tempos, corredores):
    tempos_finais = []

    for corredor in corredores:
        tempos_corredor = matriz_tempos[corredor - 1]
        tempo_final = sum(tempos_corredor)
        tempos_finais.append((corredor, tempo_final))

    # Ordena a lista de tuplas com base no tempo final
    tempos_finais.sort(key=lambda x: x[1])

    return tempos_finais

def volta_media_mais_rapida(matriz_tempos):
    medias_por_volta = np.mean(matriz_tempos, axis=0)
    volta_mais_rapida = np.argmin(medias_por_volta) + 1
    return volta_mais_rapida

# Geração automática de tempos aleatórios para cada piloto
corredores = range(1, 7)
voltas = 10

# Definindo a semente para reproducibilidade
np.random.seed(42)

matriz_tempos = np.random.uniform(low=60, high=180, size=(len(corredores), voltas))

# a) Melhor volta da prova
melhor_corredor, volta_melhor_tempo = melhor_volta(matriz_tempos, corredores)
print(f"a) Melhor volta da prova: {melhor_corredor}, Volta {volta_melhor_tempo}")

# b) Classificação final
classificacao = classificacao_final(matriz_tempos, corredores)
print("b) Classificação Final:")
for posicao, (corredor, tempo_final) in enumerate(classificacao, start=1):
    print(f"{posicao}º lugar: Corredor {corredor} - Tempo Final: {tempo_final:.2f} segundos")

# c) Volta com a média mais rápida
volta_media_rapida = volta_media_mais_rapida(matriz_tempos)
print(f"c) Volta com a média mais rápida: Volta {volta_media_rapida}")

# Tabela com os tempos
headers = ["Volta"] + [f"Corredor {corredor}" for corredor in corredores]
tabela_tempos = np.column_stack([range(1, voltas + 1)] + matriz_tempos.tolist())
print("\nTabela de Tempos:")
print(tabulate(tabela_tempos, headers=headers, tablefmt="grid"))




