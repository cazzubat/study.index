# 3: Crie uma lista que contenha um valor do tipo string, um valor do tipo real,
# um valor do tipo inteiro e um valor do tipo booleano
# imprima cada um desses valores separadamente.add()

lista = set()

string = input('Insira uma string: ')
lista.add(string)

real = float(input('Insira um valor real: '))
lista.add(real)

inteiro = int(input('Insira um número inteiro: '))
lista.add(inteiro)

booleano = input('Insira um valor booleano: ').strip().lower() == 'true'
lista.add(booleano)

print("\Valores inseridos no conjunto:")

for i in lista:
    print(i)