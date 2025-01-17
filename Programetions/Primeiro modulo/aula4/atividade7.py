soma = 0
contador = 0

print("\033[92mDigite números inteiros para calcular a média. Digite 0 para finalizar.\033[0m")
print('''------------------------------------------------------------
      ''')

while True:
    numero = int(input('Insira um número: '))
    if numero == 0:
        break

    soma += numero 
    contador += 1

if contador > 0:
    media = soma / contador
    print(f'A media é {media}')
else:
    print('''Você não inseriu nenhum número''')