# - Crie uma função contar_vogais que receba uma string e conte quantas vogais (a, e, i, o, u) existem nela.

frase = input('Insira uma uma palavra: ')

def contar_vogais(frase):
    vogais = ('a','e','i','o','u')
    resultado = 0

    for percorrer in frase:
        if percorrer in vogais:
            resultado += 1

    return resultado

print(contar_vogais(frase))