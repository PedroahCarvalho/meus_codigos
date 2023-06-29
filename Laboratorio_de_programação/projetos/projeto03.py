import random

print("Bem-vindo ao jogo Adivinhe o número!")
print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativas += 1
    palpite = int(input("Faça seu palpite: "))

    if palpite < numero_secreto:
            print("O número correto é maior. Tente novamente!")
    elif palpite > numero_secreto:
            print("O número correto é menor. Tente novamente!")
    else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

    if tentativas == 10:
            print("Suas tentativas acabaram. Você perdeu!")
            break

