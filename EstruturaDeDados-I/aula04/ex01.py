segredo = 'caneta'.strip() # .strip() função que tiras espaços no começo e no fim
acertos = [] # lista vazia.

#inicializando lista com _ . 
for _ in range(len(segredo)):
    acertos.append('_')

while '-' in acertos:
    chute = input('qual a letra? ')
    posicao = 0
    for letra in segredo:
        print(letra)
        if chute.upper() == letra.upper():
            acertos[posicao] = chute
        posicao = posicao + 1
        if (chute not in acertos) and (chute not in erros):
            print((f' acertods {acertos}'))
            print(f'erros {erros}')
            if len(erros) > 10:
                print("enforcou! game over")
                break
    
    



print(acertos)