#entrada 
#condição =100
#while condição < 200:
    #condição + 1
    #condição / 2
    #if condição  == 0:
        #print(condição)

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

interador = min(valor1, valor2) # a função (min) retorna o menor valor dos valores apresentados.

contador_pares = 0
while interador <= max(valor1, valor2): # a função (max) retorna o maior valor dos valores apresentados.
    # e ' par, enquanto o resto de divisão por 2 e 0
    if interador%2 == 0:  # % e sinal que represendata a função (mod) que devoulve o resto da divisão.
        contador_pares += 1
        print(f'{interador}par')
    else:
        print(f'{interador} impar')
    interador = interador + 1 
    #FIM DO WHILE
print(f' temos {contador_pares} numero pares ')

