print('Calculadora SIMPLES de Números inteiros')

int1 = int(input('Insira o primeiro número: '))
int2 = int(input('Inisra o segundo número: '))
operação = input('Qual tipo calculo que você quer fazer? (soma/subtração/multiplicação/divisão): ')

if operação == 'soma':
    print(f'A soma dos números é: {int1 + int2}')
elif operação == 'subtração':
    print(f'A subtração dos números é: {int1 - int2}')
elif operação == 'multiplicação':
    print(f'A multiplicação dos números é: {int1 * int2}')
elif operação == 'divisão':
    print(f'A divisão dos números é: {int1 // int2}')
else:
    print('Operação inválida. Por favor, escolha entre soma, subtração, multiplicação ou divisão.')