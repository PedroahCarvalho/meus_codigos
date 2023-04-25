vetorPossibilidade = [True, False]
linhas=0
true=0
false=0

variaveis = input('digite se a sua variavel conten (2) ou (3) variaveis: ')
formula = input('Digite a formula: ')
if (variaveis == 2):
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

elif (variaveis == 3):
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            for c in vetorPossibilidade:
                if eval(formula):
                    resultadoF=True
                    true+=1
                else:
                    resultadoF=False
                    false+=1
                print(f'A = {a} \t b = {b} \t H ={resultadoF}')
                linhas+=1
                
if true == 0:
    print('esta formula e contraditoria')
elif false == 0:
    print('essa formula e tautologica')
else:
    print('Esta formula e satisfatoria')

print(f'Total de linha com resultado VERDADEIRO: {true}')
print(f'Total de linhas com resultado FALSO: {false}')
print(f'Total de linha da tabela: {linhas}')