def soma(valores:list, ):
    """
    input: lista de valores
     ex: valores = [3, 5, 6, 8]
    output: soma dos valores
    ex: retornar 22
    """
    aux = 0
    for valor in valores:
        aux = aux + valor
    return aux


def ola(nome):
    return f'OLA {nome}'
