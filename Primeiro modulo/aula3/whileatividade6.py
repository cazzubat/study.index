# 6 - Crie um algoritmo que ao receber uma palavra a reescreve de trás para frente.
palavra = input('insira uma palavra: ')

vezes = len(palavra) - 1
resultado = ''

while vezes >= 0:
    resultado += palavra[vezes]
    vezes -= 1
print(resultado)