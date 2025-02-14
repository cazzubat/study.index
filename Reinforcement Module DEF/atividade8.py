# - Crie uma função calcular_imc que receba o peso e altura de uma pessoa e calcule o Índice de Massa Corporal (IMC), 
# com valores padrões de peso 70 kg e altura 1.75 m.

def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calculo_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")