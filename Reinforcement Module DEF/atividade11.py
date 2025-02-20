
lista_numero = []


def maior_numero(lista): 
    return max(lista) if lista else 'lista vazia'


for i in range(4):
    numero = int(input('Insira um valor: '))
    lista_numero.append(numero)

print("O maior número é:", maior_numero(lista_numero))
