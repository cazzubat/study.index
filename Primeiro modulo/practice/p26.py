print('Fatorial')

numero = int(input('Insira um número: '))

fatorial = 1

for contador in range(1, numero + 1):
    fatorial *= contador

print(f'\nO fatorial de {numero} é {fatorial}') 