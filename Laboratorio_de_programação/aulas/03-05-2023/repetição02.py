#entrada 
#condição =100
#while condição < 200:
    #condição + 1
    #condição / 2
    #if condição  == 0:
        #print(condição)


interador = 100
contador_pares = 0
while interador <= 200:
    # e ' par, enquanto o resto de divisão por 2 e 0
    if interador%2 == 0:  # % == (mod) resto da divisão
        contador_pares += 1
        print(f'{interador}par')
    else:
        print('{interador} impar')
    interador = interador + 1 
    #FIM DO WHILE
print(f' temos {contador_pares} numero pares ')

