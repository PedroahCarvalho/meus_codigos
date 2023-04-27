def quadrado(x):
    y = x * x
    return y 
def love(a,b):
    print(f'{a} gosta de {b}')

valor_para_calculo=input('Digite um numero:')
resultado = quadrado(valor_para_calculo)
print(resultado)

nome1=input('nome 1: ')
nome2=input('nome 2: ')
love(nome1,nome2)

v1=int(input('numero 1: '))
v2=int(input('numero 2: '))
v3=int(input('numero 3: '))

total=soma(v1,v2,v3)
print(f'A soma dos numeros é {total}')