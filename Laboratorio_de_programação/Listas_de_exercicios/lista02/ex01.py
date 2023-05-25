#1-Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


while True:
    nota = float(input('escreva uma nota de : '))
    if nota >10 and nota >0:
        print('nota invalida')
    else:
        print('nota inserida com sucesso!!! ')
        break

