# - Crie uma função soma que receba dois números como parâmetros e retorne a soma deles.

numero1 = int(input('Insira o primeiro numero: '))
numero2 = int(input('Insira o segundo numero: '))

def somar():
    soma = numero1 + numero2
    return soma

print(somar())