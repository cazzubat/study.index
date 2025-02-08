# 3 - Crie uma função que realiza o somatório dos valores em uma lista.

lista = [
    (10, 2), (15, 3), (20, 5), (30, 6), (40, 8),
    (50, 10), (60, 12), (70, 14), (80, 16), (90, 18),
    (100, 20), (110, 22), (120, 24), (130, 26), (140, 28),
    (150, 30), (160, 32), (170, 34), (180, 36), (190, 38)
]

def somatorio(a, b):
    return a + b

for x, y in lista:
    print(somatorio(x, y))