# 2 - Crie uma função que recebe uma lista e imprime o primeiro e o último elemento da lista.

lista = ["pedro", "carlos", "ana", "mariana", "joão", "lucas", "paula", "rafael", "camila", "gustavo", "larissa"]

def processar_lista(lista:list):
    print(f'Primeiro item: {lista[0]} Ultimo item: {lista[-1]}')

processar_lista(lista)