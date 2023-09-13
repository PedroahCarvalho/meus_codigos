import json


db = {}
opcao = 1
while opcao != 7:
    print('============Menu=================')
    print("1 - Inserir um novo produto ")
    print("2 - Consultar um produto por código:")
    print("3 - Consultar todos os produtos")
    print("4 - Alterar o preço de um determinado produto:")
    print("5 - Aplicar um acréscimo ou desconto em todos os produtos:")
    print("6 - Excluir um registro de produto:  ")
    print("7 - Sair do programa: ")
    opcao = input("opção>>> ") 
    if opcao == 1:
        codigo = input("digite o codigo: ")
        quantidade = input("Digite o nome do produto: ")
        preco = input("Digite o preço: ")
        #disponibilidade
        dbtemp = { }
    if opcao == 2:
        print("bloco 2. CONSULTA POR CODIGO")
    if opcao == 3: 
        print("Bloco 3. consultar todos os produtos")
