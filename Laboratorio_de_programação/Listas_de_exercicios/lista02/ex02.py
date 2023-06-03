#2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.



while True:
    nome=input('Digite seu nome de ususario: ')
    senha=input('Crie uma senha: ')
    if nome == senha :
        print('ERRO: a senha deve ser diferente de nome de usuario digite novamente: ')
    else:
        print('Dados dados gravados com sucesso!')
        break

print('Fim da execução do bloco.')
