print('Senha correta')
print('O codigo só vai permtir quando digitar senha a correta')

while True:
    senha_c = '1234'
    senha = input('\nInsira a senha correta: ')

    if senha == senha_c:
        print('\nVocê entrou com sucesso.')
        break
    else:
        print('\nTente novamente.')