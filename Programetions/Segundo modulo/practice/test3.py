number1 = float(input('Insira sua nota em matematica: '))
number2 = float(input('Insira sua nota em portugues:  '))
number3 = float(input('Insira sua nota em historia: '))

def media_aritmetica():
    soma = number1 + number2 + number3
    aritmetica = soma / 3
    return aritmetica

print(f'{media_aritmetica():.2f}')