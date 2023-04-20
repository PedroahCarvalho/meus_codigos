vetorPossibilidade = [True, False]
linhas=0
true=0
false=0

formula = input('Digite a formula: ')

for a in vetorPossibilidade:
    for b in vetorPossibilidade:
        if eval(formula):
            resultadoF=True
            true+=1
        else:
            resultadoF=False
            false+=1

        print(f'A = {a} \t b = {b} \t H ={resultadoF}')
        linhas+=1
print(f'Total de linha com resultado VERDADEIRO: {true}')
print(f'Total de linhas com resultado FALSO: {false}')
print(f'Total de linha da tabela: {linhas}')
