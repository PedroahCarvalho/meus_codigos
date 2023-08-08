segredo = 'caneta'.strip() # .strip() função que tiras espaços no começo e no fim
acertos = [] # lista vazia.

#inicializando lista com _ . 
for _ in range(len(segredo)):
    acertos.append('_')

print(acertos)