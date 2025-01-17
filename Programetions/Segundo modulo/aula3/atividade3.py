# Exercício 3: Escreva um programa que solicita a idade do usuário e determina se ele é elegível para votar (18 anos ou mais).

idade = int(input('Insira sua idade para vermos se você pode votar: '))

if idade >= 18:
    print(f'Vc tem {idade}, pode votar.')
else:
    print(f'Vc tem {idade}, não pode votar.')