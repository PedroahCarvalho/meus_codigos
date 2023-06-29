temperaturas = [19, 21, 25, 22, 20, 17, 15]

dias_semana = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']

for i in range(len(temperaturas)):
    dia = dias_semana[i]
    temperatura = temperaturas[i]
    histograma = '*' * temperatura
    print(f"{dia}: {histograma}")
