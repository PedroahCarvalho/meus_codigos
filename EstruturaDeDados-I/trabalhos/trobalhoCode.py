#bibliotecas 
import json
import os

# funçoes
def gravar(arc):
    with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'a') as arquivo:
        json.dump(arc, arquivo, indent=4)



# Verificando, inciando ou carregando arquivos inportentes para o programa.
banDados = {}
if(os.path.exists('EstruturaDeDados-I/trabalhos/banco_dados.json')): # verificando se o arquivo existe.
    with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'r') as arquivo:
        banDados = json.load(arquivo)
    print("Banco de dados carregado.")
else:
    print("Arquivo não existente")
    print("criando arquivo...")
    with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'w') as arquivo:
        json.dump(banDados, arquivo)
    print("Banco de Dados incido com Sucesso.")


#programa principal
opcao = 1
while opcao != 7:
    print('============Menu=================')
    print("1 - Inserir um novo produto")
    print("2 - Consultar um produto por código")
    print("3 - Consultar todos os produtos")
    print("4 - Alterar o preço de um determinado produto")
    print("5 - Aplicar um acréscimo ou desconto em todos os produtos")
    print("6 - Excluir um registro de produto  ")
    print("7 - Sair do programa. ")
    opcao = int(input('Digite opção: '))

    if opcao == 1:
        codigo = input("Incira o codigo do produto: ")
        quantidade = input("Digite o nome do produto: ")
        preco = input("Digite o preço: ")
        #disponibilidade
        dbtemp = { }
    if opcao == 2:
        print("bloco 2. CONSULTA POR CODIGO")
    if opcao == 3: 
        print("Bloco 3. consultar todos os produtos")
