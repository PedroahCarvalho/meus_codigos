
opcao = 1
while opcao != 6:
    print('========== PROGRA DE CALCULO DE JUROS ==========')
    print('1 - juros simples: ')
    print('2 - montante')

    if opcao == 1:
        print("=== JUROS SIMPLES ===")
        capital = float(input("Digite o capital:"))
        taxjuros = float((input("Digite a taxa de juros:")))
        tempo = float(input("Digite por quanto tempo:"))
        taxa = taxjuros/100
        juros = capital * taxa * tempo
        print(juros)