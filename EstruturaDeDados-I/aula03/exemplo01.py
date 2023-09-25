
n_alunos = int(input("Digite a quntidade de alunos: "))
notas=[]

for i in range(n_alunos):
    nota = float(input("Digite as notas dos alunos: "))
    notas.append(nota)
    print(notas)

    soma = 0 
    for indice in range(len(notas)):
        soma = soma + notas[indice]
        print(f'soma parcial {soma}')

    media= sum(notas)/len(notas)
    print(f"a media é de: {media}")
