print('Classificação de Triângulos')

lado1 = int(input('Insira o primeiro lado: '))
lado2 = int(input('Insira o segundo lado: '))
lado3 = int(input('Insira o terceiro lado: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

    if lado1 == lado2 == lado3:
        print('O triangulo é Triângulo Equilátero.')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('O triangulo é Triângulo Isósceles.')
    else:
            print('O triangulo é Triângulo Escaleno')
else:
    print('Os lados fornecidos não formam um triângulo.')