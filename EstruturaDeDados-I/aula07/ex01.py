contSim = 0
tupla = ('Telefonou para a vitima? ', 'Esteve no local do crime? ', 'Mora Perto da vitima? ', 'Devia para a vitima? ', ' Ja trabalhou para a vitima? ')

for tem in tupla:
    pergunta = input(tem)
    if pergunta == 'sim':
        contSim = contSim + 1
if contSim == 2:
    print('Suspeita')
elif contSim == 3 or contSim == 4:
    print('cumplice')
elif contSim == 5:
    print('culpado')
else:
    print('inocente')