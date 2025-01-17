print('Soma de números de 1 a X')
print('Escolha um número para fazermos a soma até ele.')

numero_escolhido = int(input('\nInsira um número inteiro: '))

soma = 0

for contador in range(1, numero_escolhido + 1):
    soma += contador
    print(soma)
    if soma >= numero_escolhido:
        break