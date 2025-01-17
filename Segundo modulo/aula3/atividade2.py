# Exercício 2: Crie um programa que recebe uma string e verifica se a primeira letra é vogal.

frase = input('Insira uma palavra: ').lower()

lista = ['a','e','i','o','u']

if frase[0] in lista:
    print('tem vogal')
else:
    print('não tem vogal')