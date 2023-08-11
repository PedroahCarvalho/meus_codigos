lista = [12, -2, 4 ,8, 29 ,45, 78, 36, -17, 2, 12, 8, 3 ,3, -52,]

guardar = lista[0]
for maior in (lista):
    if maior > guardar:
        guardar=maior
print(guardar)

guardar1 = lista[0]
for maior in (lista):
    if maior < guardar1:
        guardar1=maior
print(guardar1)

#usar mod
listaPares = []
for par in lista:
    if par%2 == 0:
        listaPares.append(par)
print(listaPares)
        
contador = 0
for ocorencias in lista:
    if ocorencias == lista[0]:
        contador = contador + 1
print(f'o numero de ocorenciar foi de: {contador}')

somaMedia = 0
for media in lista:
    somaMedia = somaMedia + media
mediafinal = somaMedia / len(lista)
print(f'A media e {mediafinal}')