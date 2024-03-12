from flask import Flask, request
from ibge import busca, calcula_ocorencias ,calcular_maxima

app = Flask(__name__)

@app.route("/busca_nome")
def busca_nome():
    try:
        nome = request.args.get("nome")
        response = busca(nome)
        
        # percorrer o retorno do busca e somar todas as ocorrências do nome
        soma = 0
        for valor in response[0]["res"]:
            soma += valor.get("frequencia", 0)

        mensagem = f"A soma de todas as ocorrências do nome Jose é {soma}"
        return mensagem

    except Exception as e:
        return f"Falha na rota /busca_nome: {e}"
    
@app.route("/nome_busca")
def buscar_nome():
    try:
        nome = request.args.get("nome")
        response = busca(nome)
        soma = calcula_ocorencias(response)
        objeto_retorno = {
            "nome_procurado": nome,
            "total_ocorrencias": soma
        }
        return objeto_retorno
    except Exception as e:
        return f"Falha na rota /busca_nome: {e}"
    
@app.route("/maxima")
def buscar_maxima():
    try:
        nome = request.args.get("nome")
        response = busca(nome)
        soma = calcular_maxima(response)
        print(soma)
        objeto_retorno = {
            "nome_procurado": nome,
            "preiodo de maior ocorrecia": soma
        }
        return objeto_retorno
    except Exception as e:
        return f"Falha na rota /busca_nome: {e}"


app.run(debug=True)