# Exercício 4: Crie um programa que recebe uma string como entrada e verifica se ela começa com a letra 'A'. Imprima "Começa com A" se for verdadeiro, caso contrário, imprima "Não começa com A".

frase = input('Insira uma frase: ').lower()

if frase[0] == 'a':
    print('A Primeira letra é A.')
else:
    print('Não começa com a letra A.')