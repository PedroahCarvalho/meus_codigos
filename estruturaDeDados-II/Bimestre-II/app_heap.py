from tarefa import Task
import heapq
lista_tarefas = []

def menu():
    print("-"*30)
    print("1 - adicionar Tarefa ")
    print("2- Realizar Tarefa (remover)")
    print("3- Consultar tarefas")
    print("4- sair")

def adicionar():
    titulo = input("Digite o titulo: ")
    descricao  = input("Digite a descricao: ")
    obj = Task(titulo)
    obj.set_descricao(descricao)
    prioridade = obj.get_prioridade()
    heapq.heappush(lista_tarefas, (prioridade, obj))

def consultar():
    for iten in lista_tarefas:
        print(iten[1].info())

def realizar():
    # a terefa de "maior" prioridade
    if len(lista_tarefas) > 0:
        tarefa = heapq.heappop(lista_tarefas)
        print(tarefa)
    else: 
        print("não tem tarefa")
    

if __name__ == '__main__':
    opcao = 1
    while opcao != 4:
        menu()
        opcao = int(input("Digite a opcao: "))
        if opcao == 1:
            adicionar()
        elif opcao ==2:
            realizar()
        elif opcao == 3:
            consultar()
        elif opcao == 4:
            print("saindo")
        else:
            print("opçaõ incorreta")

# estudar sorbre heap maximas e minima
