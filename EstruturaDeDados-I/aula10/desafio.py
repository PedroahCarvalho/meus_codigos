'''
vamos supor que precisamos criar um programa para cadastrae alunos em uma escola, armezenado informaçoes como nome, idade e nota. Podemos utilizar um dicionario para representar cada aluno,  onde a chave será o numero de matriculas e o valor sera outro dicionario contendo as informaçoes do aluno
'''
cadastroAlunos = {}
opcao = 1
while opcao != 3:
    print("="*40)
    print('==== MENU DE CADASTRO=====')
    print('1 - Cadastrar novo aluno')
    print('2 - Consultar cadastro')
    print('3 - Sair do programa')
    opcao = input('>>>> ')
    if opcao == 1: 
        matricula = input('Digite a matricula')
        nome = input('Digite o nome do aluno:')
        idade = input('Digite a idade do aluno: ')
        nota = input("digite as notas:")
        cadastroAlunos = [matricula]
        
