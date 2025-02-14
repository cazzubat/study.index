# Exercício 1: Escreva um programa que recebe dois números como entrada e imprime o maior deles.

numero1 = int(input('Insira o primeiro numero: '))
numero2 = int(input('Insira o segundo numero: '))

if numero1 > numero2:
    print(f'O numero {numero1} é maior que {numero2}.')
elif numero2 > numero1:
    print(f'O numero {numero2} é maior que {numero1}.')
else:
    print('Os numeros são iguais')