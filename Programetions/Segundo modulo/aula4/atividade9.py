# 36 - Crie um algoritmo que ao ser executado recebe uma palavra,
# e exibe a mensagem "Começa com vogal" caso a palavra se inicie com uma vogal
# ou exibe a mensagem "Começa com consoante" caso a palavra não se inicie em vogal

palavra = input('Insira uma palavra: ')

vogal = ['a', 'e', 'i', 'o', 'u']

if palavra[0] in vogal:
    print('Começa com vogal')
else:
    print('Começa com consoante')