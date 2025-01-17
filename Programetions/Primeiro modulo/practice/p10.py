print('Sistema de login')

nome = input('\nInsira o usuario: ')

if nome == 'pedro':
    print('O nome está correto.')
    senha = input('Insira a senha: ')
    if senha == 'pedro1234':
        print('Acesso aceito.')
    else:
        print('Acesso negado.')
else:
    print('Acesso negado.')