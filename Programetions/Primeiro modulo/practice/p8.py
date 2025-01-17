print('Ano bissexto')

ano = int(input('\n Insira o ano: '))

# Verificar se o ano é divisível por 4
if ano % 4 == 0:
    # Verificar se o ano é divisível por 100
    if ano % 100 == 0:
        # Verificar se o ano é divisível por 400
        if ano % 400 == 0:
            print('O ano é bissexto')
        else:
            print('O ano não é bissexto')
    else:
        print('O ano é bissexto')
else:
    print('O ano não é bissexto')
