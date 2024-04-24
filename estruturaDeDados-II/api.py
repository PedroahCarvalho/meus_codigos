from flask import Flask
import codigos

app = Flask(__name__)

@app.route('/insertSort', methods=['GET'])
def insertSort():
    resposta = codigos.InsertionSort()
    return resposta

app.route('/selectionSort', methods=['GET'])
def selectionsSort():
    resposta = codigos.SelectionSort()
    return resposta

app.route('/bubbleSort', methods=['GET'])
def bubbleSort():
    resposta = codigos.BubbleSort()
    return resposta

app.route('/mergeSort', methods=['GET'])
def mergeSort():
    resposta = codigos.MergeSort()
    return resposta

app.route('/quickSort', methods=['GET'])
def quickSort():
    resposta = codigos.QuickSort()
    return resposta

if __name__ == '__main__':
    app.run()