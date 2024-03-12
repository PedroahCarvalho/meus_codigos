import requests

def busca(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    resposta = requests.get(url)
    return resposta.json()

def calcula_ocorencias(var_json):
    conteudo = var_json[0]
    resposta = conteudo.get("res", [])
    soma = []
    for elemento in resposta:
        frequencia  = elemento.get('frequencia',0)
        soma.append(frequencia)
        print(f"somA{soma}")
        somado = sum(soma)
    return somado

def calcular_maxima(var_json):
    conteudo = var_json[0]
    resposta = conteudo.get("res",[])
    maior = 0
    for elemento in resposta:
        frequencia  = elemento.get('frequencia',0)
        if frequencia > maior:
            maior = frequencia
            periodo = elemento.get('periodo', 0)
    return periodo


def calcular_minima(var_json):
    conteudo = var_json[0]
    resposta = conteudo.get("res",[])
    maior = 0
    for elemento in resposta:
        frequencia  = elemento.get('frequencia',0)
        if frequencia < maior:
            periodo = elemento.get('periodo', 0)
    return periodo




nome = busca("pedro")

p = calcular_maxima(nome)
print(p)
