#bibliotecas 
import json
import os


# Verificando, inciando ou carregando arquivos importentes para o programa.
bancoDados = {}
if(os.path.exists('EstruturaDeDados-I/trabalhos/banco_dados.json')): # verificando se o arquivo existe.
    with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'r') as arquivo:
        bancoDados = json.load(arquivo)
    print("Banco de dados carregado.")
else:
    print("Banco de dados não encontrado.")
    print("Iniciando banco de dados...")
    with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'w') as arquivo:
        json.dump(bancoDados, arquivo)
    print("Banco de Dados inicido com Sucesso.")


#programa principal
opcao = 1
while opcao != 7:
    print('========== MENU ==========')
    print("1 - Inserir um novo produto")
    print("2 - Consultar um produto por código")
    print("3 - Consultar todos os produtos")
    print("4 - Alterar o preço de um determinado produto")
    print("5 - Aplicar um acréscimo ou desconto em todos os produtos")
    print("6 - Excluir um registro de produto  ")
    print("7 - Sair do programa. ")
    opcao = int(input('Digite opção: '))


    #bloco para adiciação de novos produtos
    tmp = {}
    if opcao == 1:
        print("========== Caldastro de produtos ==========")
        cod = input("Insira o codigo do produto: ")
        codigo = cod.strip()
        if codigo in bancoDados.keys():
            print("Codigo ja existente ")
        else:
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            preco = input("Digite o preço do produto: ")
            disponibildade = False
            if quantidade > 0:
                disponibildade = True
            else:
                disponibildade = False

            bancoDados[codigo] = {'nome': nome, 'quantidade':quantidade, 'preco': preco, 'disponibilidade': disponibildade}

            with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'w') as arquivo:
                json.dump(bancoDados, arquivo, indent=4)
            print('Produto adicionado com sucesso.')


    if opcao == 2:
        print("========== CONSULTA POR CODIGO ==========")



        
    if opcao == 3: 
        print("Bloco 3. consultar todos os produtos")
    else:
        
        print("ERRO, Opção invalida!")
        