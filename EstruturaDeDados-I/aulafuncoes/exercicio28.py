import random as rnd

def calcula_media(v):   
    """
    Funcao que calcula a media dos valores de uma lista
    """
    if len(v) > 0:
        return sum(v) / len(v)
    else:
        return 0

def pesquisa(valor, lista):
    return valor in lista

def inicializa_lista(quantidade=5):
    lista = []
    for _ in range(quantidade):
        valor = rnd.randint(0, 100)
        lista.append(valor)
    return lista

def menu():
    print('='*10)
    print('1- iniciar lista aleatória')
    print('2- calcular média')
    print('3- pesquisar valor')
    print('4- sair')
    return int(input('Digite sua opção: '))

# main
if __name__ == '__main__':
    v = []
    op = 0
    while op != 4:
        op = menu()
        if op == 1:
            quantidade = int(input('Digite o número de elementos na lista: '))
            v = inicializa_lista(quantidade)
        elif op == 2:
            if not v:
                print("A lista está vazia. Inicialize-a primeiro.")
            else:
                media = calcula_media(v)
                print(f"A média é {media:.2f}")
        elif op == 3:
            if not v:
                print("A lista está vazia. Inicialize-a primeiro.")
            else:
                buscar_valor = int(input('Digite o valor a ser procurado: '))
                if pesquisa(buscar_valor, v):
                    print(f'{buscar_valor} ESTÁ presente na lista')
                else:
                    print(f'{buscar_valor} NÃO ESTÁ presente na lista')
    print('Saindo....')
