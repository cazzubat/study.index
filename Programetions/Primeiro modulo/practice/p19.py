print('Fatorial')

número = int(input('\nInsira um número para fazer o fatorial: '))

if número < 0:
    print('\nInsira um valor valido.')
else:
    fatorial = 1

    while número > 1:
        fatorial *= número
        número -= 1
    print(f'\nO fatorial é: {fatorial}')