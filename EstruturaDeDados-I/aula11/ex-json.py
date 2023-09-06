import json # biblioteca para manipular arquivo json

reg01 = {'nome': 'fulano','idade': 18 , 'matriculado': True} # {} dicionario
reg02 = {'nome':'tersano', 'idade': 12, 'matriculado': False}

dados = {'alunos':[reg01, reg02]}
print('dicionario python')
print(dados)

# dups serializa o dicionario para json #
json_str = json.dumps(dados)
print('string serizada para json')
print(json_str)
#dump serealiza para salvar em arquivo 

with open('EstruturaDeDados-I/beseDados/dados.json', 'w') as json_file: #  função que escreve ou le arquivos do "HDD"  with open('cinho/da/pasta.estencao', 'w') 'w' "write" escreve ou sobrescreve, 'a' "append" adiciona no arquivo json, 'r' "read" ler arquivo.
    json.dump(dados,json_file,indent=4)



