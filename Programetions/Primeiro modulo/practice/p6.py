print('Desconto no preço')

produto = float(input('\nInsira o valor do produto: '))
duvida = (input('Você tem desconto?(sim/não): ')).lower().strip()

if duvida == "sim":
    desconto = produto - (produto * 0.10)
    print(f'O preço do produto agora é: {desconto:.2f}')
else:
    print('Você não tem cupom.')