import numpy as np

matriz = np.arange(6,11)

matriz2 = np.array([1, 2, 3, 4, 5,])

print(f'Matriz 1 {matriz}')
print(F'Matriz 2 {matriz2}')

matriz3 = matriz + matriz2
print(f'matriz + matriz2: {matriz3}')

matriz4 = matriz - matriz2
print(f'matriz4 {matriz4}')
matriz5 = matriz * matriz2
print(f'matriz { matriz5}')
matriz6 = matriz / matriz2
print(f'matriz {matriz6}')

m8 = np.array([1, 2, 3, 4, 5])
print(f'Matriz m8: {m8}')

print(f' m8 + 2: {m8 + 2}')
print(f' m8 - 2: {m8 - 2}')
print(f' m8 * 2: {m8 * 2}')
print(f' m8 / 2: {m8 / 2}')
print(f'm8 ** 2: {m8 ** 2}')

matriz9 = np.array ([7, -3, 4, 2, 7, 3, 8, 9, 1])
print(matriz9)

m7 = matriz9 > 5
print(m7)

e