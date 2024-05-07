from tarefa import Task

obj = Task("lavar roupa")
outro = Task('fazer almoço')
outro.set_descricao("Descriçã outro objeto")

# print(obj.get_titulo())
# print(outro.tit)

print(obj.info())
print("--------------------------------------------------")
print(outro.info())
