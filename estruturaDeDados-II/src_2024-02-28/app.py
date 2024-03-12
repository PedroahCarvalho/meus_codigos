from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "aplicação online"

@app.route("/qualcula", methods=['GET'])
def qualcula_numeros():
    quantidade = int(request.args.get("qnt"))
    preco = int(request.args.get('preco'))
    return f"R$ {quantidade * preco}"
    

if __name__ == "__main__":
    app.run(debug=True)