print('Tabuada')

numero = int(input('\nInsira um numero para gerar a tabuada: '))

for tabuada in range(1,(10+1)):
    soma = numero * tabuada
    print(f'{numero} x {tabuada} = {soma}') 