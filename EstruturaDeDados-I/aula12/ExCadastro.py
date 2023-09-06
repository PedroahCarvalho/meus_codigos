"""
pronto - frutas
atributos: nome, codigo, preço, peso
    chave: codigo
    valor: nome, preco,  peso 

"""

import json

Banco_dados = {}
opcoes = 1
# preciso carregar oque estiver no arquivo
try: #tratamento de Exeção "try" signfica tente ou seja ele vai tentar executar o bloco que tenta carregar o arquivo caso esse arquivo não exista ele vai para o except disendo  que o arquivo não existe, nesse caso e especifico.
    with open('EstruturaDeDados-I/beseDados/estoque.json', 'r') as arquivo:
        Banco_dados = json.load(arquivo)
except:
    print("o arquivo não existe")


while opcoes != 4:
    print('='* 10)
    print("1 - adicionar")
    print("2 - consultar por codigo")
    print("3 - consultar todos os produtos")
    print("4 - Sair")
    opcoes = int(input("Escolha a opção: "))
    if opcoes ==1:
        print('='* 10)
        print("adicionar")
        codigo = input('digite codigo: ')
        nome =input('digite o nome do protudo: ')
        preco = input('Digite o preco do kg/ unidade: ')
        Banco_dados[codigo] = {'nome': nome, "preco": preco  }
        #adicionar no arquivo
        with open('EstruturaDeDados-I/beseDados/estoque.json', 'w') as arquivo:
            json.dump(Banco_dados,arquivo, indent=4)
        
    elif opcoes==2:
        print('-'*10)
        print("consultar por codigo")
    elif opcoes==3:
        print('-'* 10)
        print('Consultar todos')
    elif opcoes==4:
        print('-'*10)
        print("sair")
    else:
        print('-'*10)
        print('opção invalida')
print("fim do programa")