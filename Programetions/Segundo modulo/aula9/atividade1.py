# 1 - Crie uma função que recebe uma string e imprime as letras individualmente no terminal.


def separar_letras():
    palavra = input('Insira uma palavra: ')
    for letra in palavra:
        print(letra)
    

separar_letras()