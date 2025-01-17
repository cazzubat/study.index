import random
print('Adivinhe o número')
print('O programa sorteia um número entre 1 e 10.')

número_aleatorio = random.randint(1,10)

while True:
    número = int(input('\n Insira o número: '))

    if número_aleatorio == número:
        print('Parabêns, você digitou o número correto.')
        break
    else:
        print('Infelimzmente você digitou o número errado, tente novamente.')
        continue