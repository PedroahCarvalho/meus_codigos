lista = [12, -2, 4 ,8, 29 ,45, 78, 36, -17, 2, 12, 8, 3 ,3, -52,]

print("*"*30)
guardar = lista[0]
for maior in (lista):
    if maior > guardar:
        guardar=maior
print(f"Ex01 - O maior elemento é {guardar}")
print("*"*30)

guardar1 = lista[0]
for maior in (lista):
    if maior < guardar1:
        guardar1=maior
print(f"Ex02 - O menor elemento é {guardar1}")
print("*"*30)

#usar mod
listaPares = []
for par in lista:
    if par%2 == 0:
        listaPares.append(par)
print(listaPares)
print("*"*30)

contador = 0
for ocorencias in lista:
    if ocorencias == lista[0]:
        contador = contador + 1
print(f'o numero de ocorenciar foi de: {contador}')
print("*"*30)

somaMedia = 0
for media in lista:
    somaMedia = somaMedia + media
mediafinal = somaMedia / len(lista)
print(f'A media e {mediafinal:.2f}')
print("*"*30)

somaDosNegativos = 0
for negativos in lista:
    if negativos < 0:
        somaDosNegativos = negativos + somaDosNegativos
print(f"a soma dos negativos e de {somaDosNegativos}")
print("*"*30)