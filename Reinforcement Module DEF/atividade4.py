# - Crie uma função contar_vogais que receba uma string e conte quantas vogais (a, e, i, o, u) existem nela.

def contar_vogais(vogais):
    vogais = ('a','e','i','o','u')
    quantia = 0
    for letra in palavra:
        if letra in vogais:
            quantia += 1
    return quantia

palavra = input('Insira uma palavra: ').lower().strip()
print(contar_vogais(palavra))