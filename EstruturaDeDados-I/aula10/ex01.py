



estoque = {}
opcao = 1
while opcao != 3:
    print('='*30)
    print("===Menu===")
    print("1 - Adicionar")
    print('2 - Consultar')
    print('3 - Sair')
    opcao = input(">>>>")
    if opcao == 1:
        codigo = input("codigo: ")
        nome = input('Nome do produto: ')
        estoque[codigo] = nome
        print('Adicionado com sucesso!')
    elif opcao == 2:
        # vou informar o codigo e ele me retornar o nome
        codigo = input('Codigo desejado: ')
        registro = estoque[codigo]
        print(f'REGISTRO RECUPERADO:  {registro}')
    elif opcao ==3:
        print('Saindo...')