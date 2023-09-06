import json

# 'r' - abrir par leitura
# 'w' - abrir para escrita (sobrescrever)
# 'a' - abrir para escrita (anexa no fim)
with open('EstruturaDeDados-I/beseDados/dados.json', 'r') as arquivo:
    registro = json.load(arquivo)

print(registro)
print(type(registro))
