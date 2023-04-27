#função é um confunto de instrução 
def cumprimento(nome):
    print(f"old {nome}, como vai você")# (def) define uma função.
def risco():
    print('-'*30)

risco()
cumprimento('zezinho')
risco()
cumprimento("pedro")

#exemplo 02 de (def) função.

x = 'Oi como vai voce? '
msg = ': ' + x  + ' :'
print('-'*len(msg))
print(msg)
print('-'*len(msg))

x = 'E ai?'
msg= ': ' + x  + ' :'
print('-'*len(msg))
print(msg)
print('-'*len(msg))

x = 'não consinsigolernada, não consigo ler nada '
msg=  ': ' + x  + ' :'
print('-'*len(msg))
print(msg)
print('-'*len(msg))

x = 'Qual é a sua mensaguem '
msg =': ' + x  + ' :'
print('-'*len(msg))
print(msg)
print('-'*len(msg))

print(len(msg)) # (len) faz a contagem de caraqteres
print(len('Professor Girafales'))

len('obabão')# sem o (print) ele não mostra a quantidade de caracteres.


def mensagem(x):
    MSG='| '+ x +' |'
    print('-'*len(MSG))
    print('-'*len(MSG))

mensagem('oi,como vai você?! ')
mensagem('E ai?')
mensagem('obabaoobabaoobabaoobabaoobabaoobabaoobabaoobabaoobabaoobabao')
mensagem(input('Quanto é a sua mensagem? '))

#ex03

