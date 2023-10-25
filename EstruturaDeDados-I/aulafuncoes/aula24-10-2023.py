def sem_parametro():
    #sem retorno 
    print("comando 1")
    for i in range(10):
        print(i)
    print("comando 2")

def sem_parametro_com_retorno():
    print("comando 3")
    valor = input("digite s ou n")
    if valor == "s":
        return 100
    print('comando 4')

def com_paremetro_sem_retorno(valor1, valor2):
    #função vai conparar se valor1 == valor2
    
    if valor1 == valor2:
        return "são iguais"
    else:
        return "são diferentes"
    
def com_paremetro_sem_retorno(valor1, valor2):
    #função vai conparar se valor1 == valor2
    if valor1 == valor2:
        print("são iguais")
    else:
        print("são diferentes")

#PROGRAMA PRINCIPAL
if __name__=="__main__": 
    print('incio')

    #sem_parametro()# a função vai ser chamada (ivocada)

    # #numero = sem_parametro_com_retorno()# toda função que retorna algum valor, tem que ser feira para uma variavel para armazenar o valor retornado pela função.
    # print("depois da chamada da função")
    # print(numero)
    
    # auxiliar = com_paremetro_com_retorno(4.56,4.56)
    # print(auxiliar)
    # auxiliar = com_paremetro_com_retorno("chapeuzinho vermelho", "chapeuzinho")
    # print(auxiliar)
    com_paremetro_sem_retorno(8,8)


