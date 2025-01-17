print('Calculadora de IMC')

altura = float(input('\nInsira sua altura: '))
peso = float(input('Insira seu peso: '))

imc = (altura ** 2) / peso

if 40.5 <= imc <= 60.9:
    print('O seu peso é o ideal.')
elif imc < 40.5:
    print('O seu peso está abaixo da média.')
else:
    print('O seu peso está acima da média.')