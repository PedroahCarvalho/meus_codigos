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
        print(frequencia)