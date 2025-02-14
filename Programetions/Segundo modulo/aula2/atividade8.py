# 1 - Escreva um programa que recebe um número inteiro do usuário e então conte de volta desse número até 1, imprimindo cada um dos números entre o valor recebido e 1.

numero = int(input('Insira um numero: '))

while numero >= 1:
    print(numero)
    numero -= 1