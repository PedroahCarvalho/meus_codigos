
valor = int=input("Digite um valor inteiro entre 0 e 9999")
if valor >= 0 and valor <=9999:
    milhar = valor //1000
    resto =volor%1000
    centenas = resto//100
    resto = resto%100
    dezenas = resto//10
    unidades = resto%10

    if milhar ==9:
        print("nove mil" end=" ")
    elif milhar ==8:
        print("oito mil" end=" ")
    elif milhar == 7:
        print("sete mil" end=" ")
    elif milhar == 6:
        print("seis mil" end=" ")
    elif milhar == 5:
        print("cinco mil" end=" ")
    elif milhar == 4:
        print("quatro mil" end=" ")
    elif milhar == 3:
        print("tres mil" end=" ")
    elif milhar == 2:
        print("dois mil" end=" ")
    elif milhar == 1:
        print("um mil" end=" ")
    
    #centena
    if  centenas == 9:
        print("novecentos"end=" ")
    elif centenas == 8:
        print("oitocentos"end=" ")
    elif centenas == 7:
        print("setecentos"end=" ")

    #dezenas 
    if dezenas == 9:
        print("noventa"end=" ")
    elif dezenas == 8:
        print("oitenta"end=" ")

    #unidades
    if unidades ==9:
        print("nove" end=" ")
    elif unidades == 8:
        print("oito"end=" ")

else:
    print("voce digitou um valor inteiro fora do intervalo")