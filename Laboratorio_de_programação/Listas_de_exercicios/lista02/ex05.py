#5- Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliações. 
 

QntNotas = int(input('Insira  a quantidade notas a ser inseridas: '))
notas = 0
if QntNotas >= 0:
    for a in range(0,QntNotas):
        if QntNotas <= 0:
            notas = float(input('insira a sua nota: '))
        else:
            Notas = float(input('insira a proxima nota: '))
else:
    print('valor invalido!')
