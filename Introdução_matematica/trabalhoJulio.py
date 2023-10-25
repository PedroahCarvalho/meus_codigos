import math
opcaoJurosSimples = 0
opcaoPrincipal = 0
opcaoJurosComposto = 0

def menuPricipal():
    print("========== MENU PRINCIPAL ==========")
    print("1 - Juros simples.")
    print("2 - Jusros compostos.")
    print("3 - Discinto Simple")
    print("4 - Finalizar programa.")
    opcaoPrincipal = int(input("Incira sua opção: "))
    return opcaoPrincipal

def menuJurosSimples():
    print("========== MENU JUROS SIMPLES ==========")
    print("1 - Calculando o juros.")
    print("2 - Calculando o capital.")
    print("3 - Calculando a taxa.")
    print("4 - Calculando o tempo.")
    print("5 - Calculando o Montante.")
    print("6 - Voltar...<--")
    opcaoJurosSimples = int(input("incira sua opção: "))
    return opcaoJurosSimples

def conversaoDeTaxa(taxa):
    taxaConvertida = input('Deseja converter a taxa? Não(n), para A.M(m) ou lower).')
    if taxaConvertida.lower() == 'm':
        taxa /= 12
    elif taxaConvertida.lower() == 'a':
        taxa *= 12
    elif taxaConvertida.lower() != 'n':
        print('Opção inválida!')
    return taxa

def conversãoDetempo(tempo):
    tempoConvertido = input('Deseja converter o tempo? Não(n), para A.M(m), A.A(a) ou DIA(d). ')
    if tempoConvertido.lower() == 'm':
        tempo /= 12
    elif tempoConvertido.lower() == 'a':
        tempo *= 12
    elif tempoConvertido.lower() == 'd':
        tempo /= 30  
    elif tempoConvertido.lower() != 'n':
        print('Opção inválida')
    return tempo

def menuJurosComposto():
    print('========== JUROS COMPOSTOS ==========')
    print('1 - Montate.')
    print('2 - Capital.')
    print('3 - Tempo.')
    opcaoJurosComposto = input('Digite a opção: ')
    return opcaoJurosComposto


while True:
    opcaoPrincipal = menuPricipal()
    if opcaoPrincipal == 1:
        opcaoJurosSimples = menuJurosSimples()
        if opcaoJurosSimples == 1:
            print('========== Calculando juros ==========')
            capital = float(input("incira o capital: "))
            taxa = float(input("incira a taxa de juros: ")) / 100
            taxaConvertida = conversaoDeTaxa(taxa)
            tempo = float(input("Digite o tempo: "))
            tempoConvertido = conversãoDetempo(tempo)
            juros = capital * taxaConvertida * tempoConvertido
            montante = (juros + capital)
            print(f'O calculo do seu juros e de {juros:.2f} e respctivo montante é de  {montante:.2f}. ')

        if opcaoJurosSimples == 2:
            print('========== Calculando capital ==========')
            juros = float(input("incira o juros: "))
            taxa = float(input("incira a taxa de juros: ")) / 100
            taxaConvertida = conversaoDeTaxa(taxa)
            tempo = float(input("incira o tempo: "))
            tempoConvertido = tempoConvertido(tempo)
            capital = juros /(taxaConvertida * tempoConvertido)
            print(f'O capital é {capital:.2f} ')


        if opcaoJurosSimples == 3:
            print('========== Calculando taxa de juros ==========')
            juros = float(input("incira o juros"))
            capital = float(input("incira o capital: "))
            tempo = float(input("incira o tempo: "))
            tempoConvertido = conversãoDetempo(tempo)
            taxa = juros / (capital * tempoConvertido)
            print(f"A taxa juros é de {taxa:.2f}.")


        if opcaoJurosSimples == 4:
            print('========== Calculando tempo ==========')
            juros = float(input("incira o juros:"))
            capital = float(input("incira o capital: "))
            taxa = float(input("incira a taxa de juros: ")) / 100
            taxaConvertida = conversaoDeTaxa(taxa) 
            tempo = juros / (capital * taxaConvertida)
            print(f"O tempo foi de {tempo:.2f}")

        if opcaoJurosSimples == 5:
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
        opcaoJurosComposto = menuJurosComposto()

        if opcaoJurosComposto == 1:
            capital = float(input('Digite o capital: '))
            taxa = float(input('Digite a taxa em %: ')) / 100
            taxaConvertida = conversaoDeTaxa(taxa)
            tempo = float(input('Digite o tempo: '))
            tempoConvertido = conversãoDetempo(tempo)
            montanteC = capital * (1 + (taxaConvertida * tempoConvertido))
            print(f'O montante composto será de {montanteC}')

        elif opcaoJurosComposto == 2:
            montanteC = float(input('Digite o montante composto: '))
            taxa = float(input('Digite a taxa em %: ')) / 100
            taxaConvertida = conversaoDeTaxa(taxa)
            tempo = float(input('Digite o tempo: '))
            tempoConvertido = conversãoDetempo(tempo)
            capital = montanteC / (1 + taxaConvertida) ** tempoConvertido
            print(f'O capital é de {capital}')

        elif opcaoJurosComposto == 3:
            montanteC = float(input('Digite o montante composto: '))
            capital = float(input('Digite o capital: '))
            tempo = float(input('Digite o tempo: '))
            tempoConvertido = tempoConvertido(tempo)
            taxa = (montanteC / capital) ** (1 / tempoConvertido) - 1
            print(f'A taxa será de {taxa}')

        elif opcaoJurosComposto == 4:
            montanteC = float(input('Digite o montante composto: '))
            capital = float(input('Digite o capital: '))
            taxa = float(input('Digite a taxa em %: ')) / 100
            taxaConvertida = conversaoDeTaxa(taxa)
            tempo = (math.log(montanteC / capital)) / (math.log(1 + taxaConvertida))
            print(f'O tempo será de {tempo}')
    elif opcaoPrincipal == 3:
        print("========== Desconto ==========")

    elif opcaoPrincipal == 4:
        print("Finalindo programa")
        break
