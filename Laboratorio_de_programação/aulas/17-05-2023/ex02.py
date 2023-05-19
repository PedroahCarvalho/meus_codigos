"""
faça um programa para determinar o numero de digito de um numero intero positivo intermado 
"""

divisão = int(input('digite o valor de entrada: '))

if divisão >= 0:
    contador = 0
    while divisão>0:
        divisão = divisão // 10
        contador+= 1 
    print(f'tem {contador} digitos')
else:
    print('numero invalido')