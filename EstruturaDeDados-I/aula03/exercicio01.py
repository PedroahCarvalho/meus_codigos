"""
faça um programa que leia o nome de 5 pessoas e armazene em uma lista de nomes. No final imprima na tela uma mensaguem de boas vindas para cada nome armazenado.
Ex: 
nome = ["turing", "ada", "linus", "Dijkstra", "bernes-Lee"]
seja bem vindo(a) Turing
seja bem vindo(a) Ada
seja bem vindo(a) Linux
seja bem vindo(a) Dijkstra
seja bem vindo(a) Berners-Lee

"""

lista =[]
n_pessoas= int(input("Quantas nomes serão inseridos?: "))
print("*"*30)

for a in range(n_pessoas):
    nome = input('Digite um nome: ')
    lista.append(nome)
    print(lista)

for boasVindas in lista:
    print(f'Boas vindas {boasVindas} !!!')