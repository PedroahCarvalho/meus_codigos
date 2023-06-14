#3- Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.



def CntBaixo():
    contador=0
    for contador in range(1, 21):
        print(contador )
        contador+= 1


def CntVertical():
    contador=0
    for contador in range(1, 21):
        print(f'{contador}', end=', ')
        contador+= 1


print('='*120)
CntBaixo()
print('='*120)
CntVertical()
