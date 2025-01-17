print('Números ímpares até X')

número = int(input('Insira o número: '))

if número < 0:
    print('\nInsira um valor válido.')
else:
    impares = 1  # Começamos com o primeiro número ímpar
    
    while impares <= número:  # Enquanto o número ímpar for menor ou igual ao número inserido
        print(impares)  # Imprime o número ímpar
        impares += 2  # Aumenta 2 para pegar o próximo ímpar
