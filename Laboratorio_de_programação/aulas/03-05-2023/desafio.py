"""
DESAFIO
com fazer para contar a quantidade de numeros pares entre dois numeros quaisquer?
"""

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

interador = min(valor1, valor2) 

contador_pares = 0
while interador <= max(valor1, valor2): 
    if interador%2 == 0:  
        #contador_pares += 1
        soma = soma + interador
    interador = interador + 1 
    #FIM DO WHILE
print(f' temos {contador_pares} numero pares ')