""" with open ('2º bimestre/14112023/arquivos/entrada.txt', 'r') as arquivo:
    num1 = int(arquivo.readline())
    num2 = int(arquivo.readline())

soma = num1 + num2
print(soma) """

arquivo = "2º bimestre/14112023/arquivos/entrada.txt"

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
    valores = leitura(arquivo)
    return sum(valores)

# EXERCICIOS 16/11/2023 
def maior_valor_arquivo():
    valores = leitura(arquivo)
    return max(valores)

def multiplica_valores_arquivo():
    valores = leitura(arquivo)
    resultado = 1
    for i in valores:
        resultado *= i
    return resultado

if __name__ == '__main__':
    valores = leitura(arquivo)
    soma = soma_valores_arquivo()
    print(f'A soma de {valores} é: {soma}')
    maior = maior_valor_arquivo()
    print(f'A maior número de {valores} é: {maior}')
    multiplicacao = multiplica_valores_arquivo()
    print(f'Os números {valores} multiplicados é: {multiplicacao}')

