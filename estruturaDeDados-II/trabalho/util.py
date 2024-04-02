import requests 

def busca_por_uf():
    # url = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/distritos'
    ufs_brasil = [
        "AC",  # Acre
        "AL",  # Alagoas
        "AP",  # Amapá
        "AM",  # Amazonas
        "BA",  # Bahia
        "CE",  # Ceará
        "DF",  # Distrito Federal
        "ES",  # Espírito Santo
        "GO",  # Goiás
        "MA",  # Maranhão
        "MT",  # Mato Grosso
        "MS",  # Mato Grosso do Sul
        "MG",  # Minas Gerais
        "PA",  # Pará
        "PB",  # Paraíba
        "PR",  # Paraná
        "PE",  # Pernambuco
        "PI",  # Piauí
        "RJ",  # Rio de Janeiro
        "RN",  # Rio Grande do Norte
        "RS",  # Rio Grande do Sul
        "RO",  # Rondônia
        "RR",  # Roraima
        "SC",  # Santa Catarina
        "SP",  # São Paulo
        "SE",  # Sergipe
        "TO"   # Tocantins
    ]
    cidades_por_uf = {}
    for uf in ufs_brasil:
        respose = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/distritos')
        resposta = respose.json()
        temp = []
        for lista in resposta:
            nomeMunicipio = lista["nome"]
            temp.append(nomeMunicipio)
        cidades_por_uf[f"{uf}"] = temp
    return cidades_por_uf



def buscar_todas():
    url = f'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
    response = requests.get(url)
    lista_cidades = []
    for cidade in response.json():
        resCidades = cidade["municipio"]
        municipio = resCidades["nome"]
        lista_cidades.append(municipio)
        print(municipio)
    print(lista_cidades)
    return lista_cidades



if __name__ == "__main__":
    res = busca_por_uf()
    print(res)


