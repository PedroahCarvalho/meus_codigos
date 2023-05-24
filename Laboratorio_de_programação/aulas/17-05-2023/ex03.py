"""
faça um programa para calcular a serie de fibonacci para numero 
informado pelo usuario, sendo F(0) = 0, F(n)= F(n-1) + F(n-2) Por exemplo, caso usuario informe o numero 
"""

fib = int(input('Digite o numeior de sequencia: '))
a= 0
b=1

if fib  >= 0:
    print(a, end=', ')
if fib >= 1:
    print(b , end=', ')
else:
    print(a, end=', ') 
    print(b, end=', ')
    for cont in range(1, fib):
        c = a + b 
        a = b
        b = c
        print(c , end=', ')
