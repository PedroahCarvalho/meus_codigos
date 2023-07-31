<<<<<<< HEAD
import random
import requests
import os

tentativas = 10



=======
""""
Desenvolva um jogo da forca em Python, no qual o programa escolhe aleatoriamente uma palavra secreta de um conjunto pré-definido. O jogador deve tentar adivinhar a palavra digitando letras. Se a letra estiver na palavra secreta, ela deve ser revelada nas posições corretas. Caso contrário, o jogador perde uma vida. O jogo continua até que o jogador adivinhe corretamente a palavra secreta ou perca todas as vidas. O número máximo de vidas deve ser definido pelo programador. O jogo deve exibir uma “representação” da forca conforme o jogador erra letras. Ao final do jogo, o programa deve informar se o jogador venceu ou perdeu, e perguntar se deseja jogar novamente. 
"""
import os
import requests
import random

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
response = requests.get(url)

palavras = response.text.split('\n')
secreta = random.choice(palavras).upper()
# print(secreta)
# secreta = 'SISTEMAS'
secreta = secreta.upper()
palavra = '*' * len(secreta)
vidas = 10
digitadas = ''
print(palavra)

while vidas > 0:
    letra = input('Digite uma letra: ').upper()

    if letra in digitadas:
        print('Essa letra já foi digitada. Tente novamente.\n')
        continue
    else:
        digitadas += letra

    acertou = False
    auxiliar = list(palavra)
    for i in range(len(secreta)):
        if letra == secreta[i]:
            auxiliar[i] = letra
            acertou = True

    palavra = ''.join(auxiliar)
    os.system('clear')
    print(palavra)

    if not acertou:
        vidas -= 1

    if palavra == secreta:
        print('Parabéns! Você acertou a palavra secreta!\n')
        break

    print('Letras digitadas:', digitadas)
    print('Vidas restantes:', vidas, '\n')

if vidas == 0:
    print('Você perdeu! A palavra secreta era:', secreta, '\n')
>>>>>>> cd818671dfa4240d482ae30b8b369b95211edf99
