print('Soma de pares')
print('Digite até que número você quer que some.')

número = int(input('\nInsira um número: '))
contagem = 0
soma = 0

while contagem <= número:
    contagem += 1
    if contagem % 2 == 0:
        soma += contagem
        print(soma)


