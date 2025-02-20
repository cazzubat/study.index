# - Crie uma função chamada calculadora que receba três parâmetros: dois números e uma operação (como uma string: "soma", "subtração", "multiplicação", "divisão"). A função deve retornar o resultado da operação escolhida entre os dois números.

def calculadora(calculo,x, y):
    if calculo == 'soma':
        return x + y
    elif calculo == 'subtração':
        return x - y
    elif calculo == 'multiplicação':
        return x * y
    elif calculo == 'divisão':
        return x / y if y != 0 else 'erro: não da pra se dividir por zero'
    else:
        return 'Insira um valor valído.'

calcular = input('Insira um calculo que deseja fazer: ')
number1 = float(input('Insira o primeiro valor: '))
number2 = float(input('Insira o segundo valor: '))

print(calculadora(calcular, number1, number2))