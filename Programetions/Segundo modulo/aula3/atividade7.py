# - Crie uma função calcular_imc que receba o peso e altura de uma pessoa e calcule o Índice de Massa Corporal (IMC), com valores padrões de peso 70 kg e altura 1.75 m.

peso = float(input('Insira seu peso: '))
altura = float (input('Insira sua altura: '))

def calcular_imc():
    imc = peso / altura ** 2
    return imc

print(f'{calcular_imc():.2f}')