import math
opcaoJurosSimples = 0
opcaoPrincipal = 0

def menuPricipal():
    print("========== MENU PRINCIPAL ==========")
    print("1 - Juros simples.")
    print("2 - Jusros compostos.")
    print("3 - Finalizar programa.")
    opcaoPrincipal = int(input("Incira sua opção: "))

def menuJurosSimples():
    print("========== MENU JUROS SIMPLES ==========")
    print("1 - Calculando o juros.")
    print("2 - Calculando o capital.")
    print("3 - Calculando a taxa.")
    print("4 - Calculando o tempo.")
    print("5 - Calculando o Montante.")
    print("6 - Voltar...<--")
    opcaoJurosSimples = int(input("incira sua opção: "))

while True:
    menuPricipal()

    if opcaoPrincipal == 1:
        menuJurosSimples()
        if opcaoJurosSimples == 1:#juros
            print('========== Calculando juros ==========')
            capital = float(input("incira o capital: "))
            taxa = float(input("incira a taxa de juros: ")) / 100
            taxaConvertida = input('Deseja converter a taxa? Não(n), para A.M(m) ou A.A(a). ')
            if taxaConvertida.lower() == 'm':
                taxa /= 12
            elif taxaConvertida.lower() == 'a':
                taxa *= 12
            elif taxaConvertida.lower() != 'n':
                print('Opção inválida!')
                # continue
            tempo = float(input("Digite o tempo: "))
            tempoConvertido = input('Deseja converter o tempo? Não(n), para A.M(m), A.A(a) ou DIA(d). ')
            if tempoConvertido.lower() == 'm':
                tempo /= 12
            elif tempoConvertido.lower() == 'a':
                tempo *= 12
            elif tempoConvertido.lower() == 'd':
                tempo /= 30  
            elif tempoConvertido.lower() != 'n':
                print('Opção inválida')
                # continue
            juros = capital * taxa * tempo
            montante = (juros + capital)
            print(f'O calculo do seu juros e de {juros:.2f} e respctivo montante é de  {montante:.2f}. ')

        if opcaoJurosSimples == 2:#capital c=i*t/j
            print('========== Calculando capital ==========')
            juros = float(input("incira o juros: "))
            taxa = float(input("incira a taxa de juros: ")) / 100
            taxaConvertida = input('Deseja converter a taxa? Não(n), para A.M(m) ou lower).')
            if taxaConvertida.lower() == 'm':
                taxa /= 12
            elif taxaConvertida.lower() == 'a':
                taxa *= 12
            elif taxaConvertida.lower() != 'n':
                print('Opção inválida!')
                # continue
            tempo = float(input("incira o tempo: "))
            tempoConvertido = input('Deseja converter o tempo? Não(n), para A.M(m), A.A(a) ou DIA(d). ')
            if tempoConvertido.lower() == 'm':
                tempo /= 12
            elif tempoConvertido.lower() == 'a':
                tempo *= 12
            elif tempoConvertido.lower() == 'd':
                tempo /= 30  
            elif tempoConvertido.lower() != 'n':
                print('Opção inválida!')
                continue
            capital =   juros /(taxa * tempo)
            print(f'O capital é {capital:.2f} ')


        if opcaoJurosSimples == 3:#taxa i=c*t/j
            print('========== Calculando taxa de juros ==========')
            juros = float(input("incira o juros"))
            capital = float(input("incira o capital: "))
            tempo = float(input("incira o tempo: "))
            tempoConvertido = input('Deseja converter o tempo? Não(n), para A.M(m), A.A(a) ou lower). ')
            if tempoConvertido.lower() == 'm':
                tempo /= 12
            elif tempoConvertido.lower() == 'a':
                tempo *= 12
            elif tempoConvertido.lower() == 'd':
                tempo /= 30  
            elif tempoConvertido.lower() != 'n':
                print('Opção inválida!')
                # continue
            taxa = juros / (capital * tempo)
            print(f"A taxa juros é de {taxa:.2f}.")


        if opcaoJurosSimples == 4:#tempo c*i/j=t
            print('========== Calculando tempo ==========')
            juros = float(input("incira o juros:"))
            capital = float(input("incira o capital: "))
            taxa = float(input("incira a taxa de juros: ")) / 100
            taxaConvertida = input('Deseja converter a taxa? Não(n), para A.M(m) ou lower). ')
            if taxaConvertida.lower() == 'm':
                taxa /= 12
            elif taxaConvertida.lower() == 'a':
                taxa *= 12
            elif taxaConvertida.lower() != 'n':
                print('Opção inválida!')
            tempo = juros / (capital * taxa)
            print(f"O tempo foi de {tempo:.2f}")

        if opcaoJurosSimples == 5:#montante
            print('========== Calculando o montante ==========')
            capital = float(input("incira o capital: "))
            juros = float(input("incira a taxa em %: "))
            montante = capital + juros
            print(f'O montante é de {montante:.2f}. ')

        elif opcaoJurosSimples == 6:
            menuPricipal()

        else:
            print('Opção inválida, escolha uma opção válida.')
            continue

    elif opcaoPrincipal == 2:

        calcular = input('Digite o que você deseja calcular: Montante (M), Capital (C), Taxa (I) ou Tempo (T): ')

        if calcular.upper() == 'M':
            capital = float(input('Digite o capital: '))
            taxa = float(input('Digite a taxa em %: ')) / 100
            taxaConvertida = input('Deseja converter a taxa? Não (N), para A.M (M) ou A.A (A): ')

            if taxaConvertida.upper() == 'N':
                taxa = taxa
            elif taxaConvertida.upper() == 'M':
                taxa = taxa / 12
            elif taxaConvertida.upper() == 'A':
                taxa = taxa * 12
            else:
                print('Opção inválida, escolha N, M ou A.')

            tempo = float(input('Digite o tempo: '))
            tempoConvertido = input('Deseja converter o tempo? Não (N), para A.M (M) ou A.A (A): ')

            if tempoConvertido.upper() == 'N':
                tempo = tempo
            elif tempoConvertido.upper() == 'M':
                tempo = tempo / 12
            elif tempoConvertido.upper() == 'A':
                tempo = tempo * 12
            else:
                print('Opção inválida, escolha N, M ou A.')

            montanteC = capital * (1 + (taxa* tempo))
            print(f'O montante composto será de {montanteC}')

        elif calcular.upper() == 'C':
            montanteC = float(input('Digite o montante composto: '))
            taxa = float(input('Digite a taxa em %: ')) / 100
            taxaConvertida = input('Deseja converter a taxa? Não (N), para A.M (M) ou A.A (A): ')

            if taxaConvertida.upper() == 'N':
                taxa = taxa
            elif taxaConvertida.upper() == 'M':
                taxa = taxa / 12
            elif taxaConvertida.upper() == 'A':
                taxa = taxa * 12
            else:
                print('Opção inválida, escolha N, M ou A.')

            tempo = float(input('Digite o tempo: '))
            tempoConvertido = input('Deseja converter o tempo? Não (N), para A.M (M) ou A.A (A): ')

            if tempoConvertido.upper() == 'N':
                tempo = tempo
            elif tempoConvertido.upper() == 'M':
                tempo = tempo / 12
            elif tempoConvertido.upper() == 'A':
                tempo = tempo * 12
            else:
                print('Opção inválida, escolha N, M ou A.')

            capital = montanteC / (1 + taxa) ** tempo
            print(f'O capital é de {capital}')

        elif calcular.upper() == 'I':
            montanteC = float(input('Digite o montante composto: '))
            capital = float(input('Digite o capital: '))
            tempo = float(input('Digite o tempo: '))
            tempoConvertido = input('Deseja converter o tempo? Não (N), para A.M (M) ou A.A (A): ')

            if tempoConvertido.upper() == 'N':
                tempo = tempo
            elif tempoConvertido.upper() == 'M':
                tempo = tempo / 12
            elif tempoConvertido.upper() == 'A':
                tempo = tempo * 12
            else:
                print('Opção inválida, escolha N, M ou A.')

            taxa = (montanteC / capital) ** (1 / tempo) - 1
            print(f'A taxa será de {taxa}')

        elif calcular.upper() == 'T':
            montanteC = float(input('Digite o montante composto: '))
            capital = float(input('Digite o capital: '))
            taxa = float(input('Digite a taxa em %: ')) / 100
            taxaConvertida = input('Deseja converter a taxa? Não (N), para A.M (M) ou A.A (A): ')

            if taxaConvertida.upper() == 'N':
                taxa = taxa
            elif taxaConvertida.upper() == 'M':
                taxa = taxa / 12
            elif taxaConvertida.upper() == 'A':
                taxa = taxa * 12
            else:
                print('Opção inválida, escolha N, M ou A.')

            tempo = (math.log(montanteC / capital)) / (math.log(1 + taxa))
            print(f'O tempo será de {tempo}')
