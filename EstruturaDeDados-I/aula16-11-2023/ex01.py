
def leitura(nome_arquivo: str):
    try:
        lista = []
        with open(nome_arquivo, 'r') as arquivo:
            arquivo.seek(0) # posicionando cursor no inicio
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    valor =  float(linha)
                    lista.append(valor)
            return lista
    except Exception as e:
        print("Houve uma falha na abertura do arquivo")
        print(e)
        return None

def soma_valores_arquivo():
    valores = leitura("C:\\Users\\Libertas\\Documents\\GitHub\\meus_codigos\\DesenvolvimentoWeb_II\\aula16-11-2023\\entrada.txt")
    print(valores)
    return sum(valores)

# EXERCICIOS 16/11/2023 
def maior_valor_arquivo(lista):
    t = 0
    for i in lista:
        if i > t:
            t = i
    return t


def multiplica_valores_arquivo(lista):
    t =  1
    for i in lista:
        t = t * i
    return t

if __name__ == '__main__':
    lista = leitura("C:\\Users\\Libertas\\Documents\\GitHub\\meus_codigos\\DesenvolvimentoWeb_II\\aula16-11-2023\\entrada.txt")
    print(lista)
    soma = soma_valores_arquivo()
    print(soma)
    maior = maior_valor_arquivo(lista)
    print(maior)
    multiplicar = multiplica_valores_arquivo(lista)
    print(multiplicar)

