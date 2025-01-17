print('Lista de nomes')

lista = []

nome1 = lista.append(input('Adicione o primeiro nome na lista: '))
nome2 = lista.append(input('Adicione o segundo nome na lista: '))
nome3 = lista.append(input('Adicione o terceiro nome na lista: '))
nome4 = lista.append(input('Adicione o quarto nome na lista: '))
nome5 = lista.append(input('Adicione o quinto nome na lista: '))

for posicao in range(len(lista)):
    print(f"\n{posicao + 1}º {lista[posicao]}")