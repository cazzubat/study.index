print("Soma de números positivos inteiros! Quando quiser parar o código, digite 0.")

soma = 0

while True:
    ligar = int(input('\nInsira um número positivo: '))

    if ligar == 0:
        break

    if ligar < 0:
        print('Número invalido, tente novamente.')
        continue

    soma += ligar
    print(f'O valor da soma até agora é: {soma}')
print(f'O valor final da soma é: {soma}')

