op = input('Deseja somar (S) ou multiplicar (m)?')
op = op.strip().upper()
if (op == 'S' or op == 'M'):
    x = float(input('Digite o primeiro numero: '))
    y = float(input('Digite o seguendo numero: '))
    if (op == 'S'):
        r = x + y
    else:
        r = x * y
    print('O resultado é', r)
else:
    print('Opção invalida!')
    
# .strip função para tirar espaços 
# .upper função para trasformar em letra maiuscula 
# pass significa que irei implemantar depois 
