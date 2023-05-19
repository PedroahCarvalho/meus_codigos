
"""
for contador in range(1,11):
    print("="*20)
    print(f'Tabuada do {contador}')
    for fator in range(1,11):
        resultado = contador*fator
        print(f '{contador}x {fator} \t=\t{resultado}')

""""""
faça um programa para determinar o numero de digito de um numero intero positivo intermado 
"""
divisão = int(input('digite o valor de entrada: '))
contador = 0
while divisão>0:
    divisão = divisão // 10
    contador+= 1 
print(f'tem {contador} digitos')