

# nome_aluno = input("Digite o nome do aluno: ")

# soma_notas = 0
# contador_notas = 0

# while True:
#     nota = input("Digite a nota do aluno (ou digite 'fim' para encerrar: ")
#     if nota.lower() == 'fim':
#         break
    
#     nota = float(nota)
#     soma_notas += nota
#     contador_notas += 1

# media = soma_notas / contador_notas

# print("Nome do aluno:", nome_aluno)
# print("Média:", media)

# n = 10
# fatorial = 1

# for i in range(1, n + 1):
#     fatorial *= i

# print("O fatorial de", n, "é", fatorial)


primeiro=0
sugundo= 0
terceiro=0
lista = list()
for intem in range(0,10):
    print('primeiro for')
    primeiro+= 1
    for subintens in range(0,10):
        lista.append(subintens)
        print('segundo for')
        sugundo+= 1
    for subitem in lista:
        print('subitens')
        print('terceiro for')
        terceiro+=1
        if (subintens == 5):
            break
print(primeiro)
print(sugundo)
print(terceiro)



