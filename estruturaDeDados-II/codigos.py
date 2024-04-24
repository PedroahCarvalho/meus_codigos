import requests
import time
import random

def buscar():
    url ='https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
    r = requests.get(url)
    return r.json()


def InsertionSort():
    lista = buscar()
    arr = []
    for cidade in lista:
        resCidades = cidade["municipio"]
        municipio = resCidades["nome"]
        arr.append(municipio)
    random.shuffle(arr)# desordenado a lista ordenada da requisição
    comp = 0  # Contador de comparações
    start_time = time.time()  # Marca o início da execução
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comp += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    end_time = time.time()  # Marca o fim da execução
    exec_time = end_time - start_time  # Calcula o tempo de execução
    # print(f'InsertionSort: , numereros de conparaçôes: {comp},tempo de execução: {exec_time}.')
    
    return f'InsertionSort: numereros de conparaçôes: {comp},tempo de execução: {exec_time}.'
            
def SelectionSort():
    lista = buscar()
    arr = []
    for cidade in lista:
        resCidades = cidade["municipio"]
        municipio = resCidades["nome"]
        arr.append(municipio)

    random.shuffle(arr)# desordenado a lista ordenada da requisição
    comparacoes = 0
    inicio = time.time()  # Captura o tempo de início da execução
    n = len(arr)
    for i in range(n):
        menor_idx = i
        for j in range(i+1, n):
            comparacoes += 1
            if arr[j] < arr[menor_idx]:
                menor_idx = j
                
        arr[i], arr[menor_idx] = arr[menor_idx], arr[i]
    
    fim = time.time()  # Captura o tempo de fim da execução
    tempo_execucao = fim - inicio
    # print(f' lista ordenas selctionSort: , numereros de conparaçôes: {comparacoes},tempo de execução: {tempo_execucao}.')
    return f'SelectionSort:,numereros de conparaçôes: {comparacoes},tempo de execução: {tempo_execucao}.'

def BubbleSort():
    lista = buscar()
    arr = []
    for cidade in lista:
        resCidades = cidade["municipio"]
        municipio = resCidades["nome"]
        arr.append(municipio)
    random.shuffle(arr)# desordenado a lista ordenada da requisição
    comp = 0  # Contador de comparações
    start_time = time.time()  # Marca o início da execução
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    end_time = time.time()  # Marca o fim da execução
    exec_time = end_time - start_time  # Calcula o tempo de execução
    return f'BubbleSort: numereros de conparaçôes: {comp},tempo de execução: {exec_time}.'

def MergeSort():
    resp = buscar()
    arr = []
    for cidade in resp:
        resCidades = cidade["municipio"]
        municipio = resCidades["nome"]
        arr.append(municipio)
    random.shuffle(arr)# desordenado a lista ordenada da requisição
    comp = [0]  # Contador de comparações
    start_time = time.time()  # Marca o início da execução
    
    def partition(arr, low, high):
        comp[0] += 1
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    
    end_time = time.time()  # Marca o fim da execução
    exec_time = end_time - start_time  # Calcula o tempo de execução
    
    return f'MergeSort: numeros de comparaçôes: {comp[0]}, ,tempo de execução: {exec_time}'



def QuickSort():
    resp = buscar()
    arr = []
    for cidade in resp:
        resCidades = cidade["municipio"]
        municipio = resCidades["nome"]
        arr.append(municipio)
    random.shuffle(arr)# desordenado a lista ordenada da requisição

    comp = [0]  # Contador de comparações
    start_time = time.time()  # Marca o início da execução
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comp[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)
    
    quick_sort_helper(arr, 0, len(arr) - 1)
    
    end_time = time.time()  # Marca o fim da execução
    exec_time = end_time - start_time  # Calcula o tempo de execução
    
    return f'QuickSort: numeros de comparaçôes: {comp[0]}, tempo de execução:  {exec_time}'

if __name__ == '__main__':
    def1 = InsertionSort()
    print(def1)
    SelectionSort()
    def2 = SelectionSort()
    print(def2)
    def3 = BubbleSort() 
    print(def3)
    def4 =  MergeSort()
    print(def4)
    def5 =  QuickSort()
    print(def5)



   


