#0 : Através do exemplo do contador de letras, crie um algoritmo que exiba cada letra de uma palavra digitada pelo usuário;

palavra = input('insira a palavra: ')
n = 0

while n <len(palavra):
    print(palavra [n])
    n += 1