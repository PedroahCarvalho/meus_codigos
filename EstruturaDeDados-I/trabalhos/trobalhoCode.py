#bibliotecas 
import json
import os

# funçoes
def gravar(arc):
    with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'a') as arquivo:
        json.dump(arc, arquivo, indent=4)



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
        codigo = input("Incira o codigo do produto: ")
        if codigo in bancoDados.keys():
            print("Codigo ja existe ")
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


    elif opcao == 2:
        print("========== CONSULTA POR CODIGO ==========")
        codigo = input('Digite o codigo do produto: ')
        if codigo in bancoDados.keys():
            produto = bancoDados[codigo]
            print(f'Codigo: {codigo} | Produto: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]}')
            #print(bancoDados) 
        else:
            print("ERRO, Codigo não encontrado.")


    elif opcao == 3: 
        print("========== PRODUTOS CADASTRADOS ==========")
        for i in bancoDados:
            produto = bancoDados[i]
            print(f'Codigo: {i} | Produto: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]}')
    

    elif opcao == 4:
        print("bloco 4")









    else:
        
        print("ERRO, Opção invalida!")
