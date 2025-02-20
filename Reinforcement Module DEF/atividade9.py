#  - Crie uma função chamada fatorial que calcule o fatorial de um número.

def fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

numero = int(input('Digite um numero para fatorar: '))
print(f'O fatorial do número {numero} é {fatorial(numero)}')