

opcao = 1
while opcao != 6:
    print('========== PROGRA DE CALCULO DE JUROS ==========')
    print('1 - juros simples: ')
    print('2 - montante')

    if opcao == 1:
        print("=== JUROS SIMPLES ===")
        capital = input("Digite o capital:")
        taxjuros = input("Digite a taxa de juros")
        tempo = input("Digite por quanto tempo:")
        #j = c * i * t
        juros = capital * taxjuros * tempo
        print(f'Seu juros sera de {juros}')

    elif opcao == 2:
        print('')
        capital = input("Digite o capital: ")
        juros  = input("Digite o juros: ")
        montante = capital + juros
        

def jurosSimple(capital, taxaJuros, tempo)
        #j = c * i * t
        juros = capital * taxaJuros * tempo
        return juros
    