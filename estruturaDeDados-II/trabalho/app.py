from flask import Flask, jsonify
from util import busca_por_uf, buscar_todas

app = Flask(__name__)

@app.route('/cidades/brasil', methods=['GET'])
def cidade_brasil():
    cidades = buscar_todas()
    return jsonify(
        cidades
    )

@app.route('/cidades/uf', methods=['GET'])
def cidade_por_uf():
    resposta = busca_por_uf()
    return jsonify(
        resposta
    )


if __name__ == '__main__':
    app.run(debug=False)