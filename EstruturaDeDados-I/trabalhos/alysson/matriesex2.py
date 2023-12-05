"""2- Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um
número k. Imprima a matriz na tela antes e depois da multiplicação."""

import numpy as np

def multiplicar_diagonal_principal(matriz, k):
    diagonal_principal = np.diag(matriz)
    matriz_resultante = matriz.copy()
    np.fill_diagonal(matriz_resultante, diagonal_principal * k)
    return matriz_resultante

# Lendo a matriz do usuário
matriz_usuario = []
for i in range(3):
    linha = list(map(int, input(f"Digite os elementos da linha {i + 1} separados por espaço: ").split()))
    matriz_usuario.append(linha)

matriz_usuario = np.array(matriz_usuario)

# Lendo o valor de k do usuário
k = float(input("Digite o valor de k: "))

# Exibindo a matriz original
print("Matriz Original:")
print(matriz_usuario)

# Chamando a função e exibindo a matriz resultante
matriz_resultante = multiplicar_diagonal_principal(matriz_usuario, k)
print(f"Matriz Após Multiplicação pela Diagonal Principal (k = {k}):")
print(matriz_resultante)
