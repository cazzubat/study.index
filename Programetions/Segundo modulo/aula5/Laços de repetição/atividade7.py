# 7 - Crie um algoritmo que ao receber um número calcule a tabuada deste número até 10 e exiba cada uma das multiplicações no terminal
# Ex: numero = 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

numero = int(input("Digite um número: "))

for percorrer in range(1, 11):
    print(f'{numero} x {percorrer} = {numero * percorrer}')