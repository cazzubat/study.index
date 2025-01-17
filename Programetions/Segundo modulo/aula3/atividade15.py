# 1: Crie um algoritmo que, ao declararmos uma lista com o nome de três amigos, imprima:
# o nome do primeiro amigo
# o nome do segundo amigo
# o nome do terceiro amigo

lista = []

for amigo in range(3):
    amigo = input(f'Adicione o seu {amigo + 1}º amigo: ')
    lista.append(amigo)

print('\nLista do seus amigos: ')
print(lista)