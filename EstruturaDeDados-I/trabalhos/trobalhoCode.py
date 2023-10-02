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

    #bloco que faz consulta por codigo
    elif opcao == 2:
        print("========== CONSULTA POR CODIGO ==========")
        codigo = input('Digite o codigo do produto: ')
        if codigo in bancoDados.keys(): #vericindo se protuto consta na base de dados.
            produto = bancoDados[codigo]
            #imprimindo produto selecionado. 
            print(f'Codigo: {codigo} | Produto: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]}')
        else:
            print("ERRO, Codigo não encontrado.")

    elif opcao == 3: 
        print("========== PRODUTOS CADASTRADOS ==========")
        for i in bancoDados:
            produto = bancoDados[i]
            print(f'Codigo: {i} | Produto: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]}')
    
    elif opcao == 4:
        print("========== ALTERAÇÃO DE TEXTOS ==========")
        codigo = input('Digite o codigo que de deseja alterar: ')
        if codigo in bancoDados.keys():
            produto = bancoDados[codigo]
            print(f"O produto selecionado é {produto['nome']} e preço atual é de R${produto['preco']}.")
            novoPreco = float(input("Insira o preço desejado: "))
            produto['preco'] = novoPreco
            with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'w') as arquivo:
                json.dump(bancoDados, arquivo, indent=4)
            print('Preço alterado com sucesso.')
        else:
            print('ERRO, Codigo não encontrado')
        
    elif opcao ==5 :
        opcaoInterna = 0
        print('========== ACRECIMO OU DECRECIMO DE PREÇO ==========')
        print('1 - Acrecimo.')
        print('2 - Decrecimo.')
        opcaoInterna = int(input('insira sua opção: '))
        if opcaoInterna == 1:
            print("========== ACRECIMO ==========")
            acrecimo = int(input("Digite de quantos porcento sera o acrecimo: "))
            decimal = acrecimo /100
            for i in bancoDados.keys():
                produto = bancoDados[i]
                preco = produto['preco']
                preco = float(preco)
                porcento = preco * decimal
                valorFinal = preco+ porcento
                print(valorFinal)
                with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'w') as arquivo:
                    json.dump(bancoDados, arquivo, indent=4)
            print('Preços modificados com sucesso.')
            #DESCONTO
        elif opcaoInterna == 2:
            print("========== DESCONTO ==========")
            acrecimo = int(input("Digite de quantos porcento sera o acrecimo:"))
            decimal = acrecimo /100
            for i in bancoDados.keys():
                produto = bancoDados[i]
                preco = produto['preco']
                porcento = float(preco) * decimal
                valorFinal = preco - porcento
                print(valorFinal)
                with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'w') as arquivo:
                    json.dump(bancoDados, arquivo, indent=4)
            print('Preços modificados com sucesso.')

        else:
            print("ERRO, opção invaida.")

    elif opcao == 6:
        print("========== EXCLUIR PRODUTOS ========== ")
        chave = input("Digite o codigo do produto a ser excluido: ")
        if chave.strip() in bancoDados.keys():
            bancoDados.pop(chave)
            with open('EstruturaDeDados-I/trabalhos/banco_dados.json', 'w') as arquivo:
                json.dump(bancoDados, arquivo, indent=4)
            print("Produto excluido com sucesso.")
        else:
            print('ERRO, produto não existente.')

    else:
        
        print("ERRO, Opção invalida!")
        