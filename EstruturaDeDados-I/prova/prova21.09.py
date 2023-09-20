import json

banco = {}

with open('EstruturaDeDados-I/prova/banco_dados.json','r') as arquivo:
    banco = json.load(arquivo)

print("ordenado em ordem alfabetica")
lista1 = []
for i in banco.keys():
    individo = banco[i]
    nome = individo['nome']
    lista1.append(nome)
    lista1.sort()
    for elem in lista1:
        print(elem)

lista02 = []
temporaria = 0
for i in banco.keys():
    individo = banco[i]
    idade = individo['idade']
    if individo['idade'] > temporaria:
        temporaria = idade
        velho = individo['nome'], individo['idade']
        lista02.append(velho)
print(lista02[-1])

lista03 = []
temporaria = 1
for i in banco.keys():
    individo = banco[i]
    idade = individo['idade']
    if individo['idade'] < temporaria:
        temporaria = idade
        velho = individo['nome'], individo['idade']
        lista03.append(velho)
print(lista03)


temporaria = 0
for i in banco.keys():
    individo = banco[i]
    salario = individo['salario']
    if individo['salario'] > temporaria:
        temporaria = salario
        print(temporaria)
        print(f'{individo['nome']}, ganha mais e sue salario e {individo['salario']}')

