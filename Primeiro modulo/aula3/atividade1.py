# Condicionais:

# 01 - Crie um algoritmo em que o usuário informe dois números (n1 e n2). Após, exiba na tela (terminal) qual deles é o maior.
number1 = float(input('insira o primeiro numero: '))
number2 = float(input('insira o segundo numero: '))

if number1 > number2:
    print('o primeiro numero é maior que o segundo')
elif number1 == number2:
    print('os numeros são iguais')
else:
    print('os o segundo numero é maior que o primeiro')