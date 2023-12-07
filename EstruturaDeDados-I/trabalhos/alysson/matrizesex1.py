"""EXERCICIOS MATRIZ: BIM2 - MATRIZES - AULA 23/11/23
1 - Programa que armazena os nomes e idades de 10 pessoas em uma matriz, e imprime o nome da pessoa mais nova
"""
import numpy as np

def pessoa_mais_nova(matriz):
    nomes = matriz[:, 0]
    idades = matriz[:, 1]
    indice_mais_novo = np.argmin(idades)
    nome_mais_novo = nomes[indice_mais_novo]
    return nome_mais_novo

# Criando a matriz de nomes e idades
nomes_idades = np.array([
    ["Ana", 25],
    ["Carlos", 20],
    ["Maria", 30],
    ["João", 22],
    ["Julia", 28],
    ["Pedro", 18],
    ["Mariana", 35],
    ["Luiz", 21],
    ["Catarina", 27],
    ["Fernando", 24]
])

# Chamando a função e exibindo o resultado
nome_mais_novo = pessoa_mais_nova(nomes_idades)
print(f"A pessoa mais nova é: {nome_mais_novo}")
