#5- Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliações. 

QntNotas = int(input('Insira  a quantidade notas a ser inseridas: '))
notas = 0
for a in range(0,QntNotas):
    n = float(input('insira sua nota:  '))
    notas+= n 
res= notas / QntNotas
print(f'Sua media e de {res}')