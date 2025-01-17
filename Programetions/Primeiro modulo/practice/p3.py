print('Calculadora simples')

n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))

calculo = input('Qual seria o calculo que você quer fazer? (+, -, *, /): ')

if calculo == '+':
    print(f'O resultado é: {n1 + 2}')
elif calculo == '-':
    print(f'O resultado é: {n1 - n2}')
elif calculo == '*':
    print(f'O resultado é: {n1 * n2}')
elif calculo == '/':
    print(f'O resultado é: {(n1 / n2):.2f}')
else:
    print('Insira um um número valido.')