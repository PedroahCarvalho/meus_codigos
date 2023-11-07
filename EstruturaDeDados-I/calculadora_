'''
Opções:
(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar memória
(6) Sair do programa
Qual opção você deseja?
'''

def menu_principal():
    print(("="*15) + " MENU CALCULADORA " + ("="*15))
    print('1 - Soma.')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Limpar memoria')
    print('6 - Sair do programa')
    opção = int(input("Qual opção você deseja?"))
    return opção

def linhas (nome = ''):
    print(f'==============='+{nome}+'===============')



#main (programa principal)
memoria_teporaria = 0 
opcao = 0
while True:
    print(f"memoria {memoria_teporaria}")
    opcao = menu_principal()
    if opcao == 1:
        print(("="*15) + " Soma " + ("="*15))
        if memoria_teporaria == 0:
            memoria_teporaria = int(input('Digite uma numero: '))
            n2 = int(input("digite outro numero: "))
            memoria_teporaria = memoria_teporaria + n2
        else:
            n = int(input('Insira um numero:'))
            memoria_teporaria = memoria_teporaria + n

    elif opcao == 2:
        print(("="*15) + " Subtração " + ("="*15))
        if memoria_teporaria == 0:
            memoria_teporaria = int(input('Digite uma numero: '))
            n2 = int(input("digite outro numero: "))
            memoria_teporaria = memoria_teporaria - n2
        else:
            n = int(input('Insira um numero:'))
            memoria_teporaria = memoria_teporaria - n
    elif opcao == 3:
        print(("="*15) + " Multiplicação " + ("="*15))
        if memoria_teporaria == 0:
            memoria_teporaria = int(input('Digite uma numero: '))
            n2 = int(input("digite o multiplicador: "))
            memoria_teporaria = memoria_teporaria * n2
        else:
            n = int(input('Insira o multiplicador:'))
            memoria_teporaria = memoria_teporaria * n
    elif opcao == 4:
        print(("="*15) + " Divisão " + ("="*15))
        if memoria_teporaria == 0:
            memoria_teporaria = int(input('Digite uma numero: '))
            n2 = int(input("digite outro numero: "))
            memoria_teporaria = memoria_teporaria / n2
        else:
            n = int(input('Insira um numero:'))
            memoria_teporaria = memoria_teporaria / n

    elif opcao == 5:
        memoria_teporaria = 0

    #sair
    elif opcao == 6:
        print('Saindo do programa')
        break


    
