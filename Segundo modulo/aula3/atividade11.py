# 4 - Escreva um programa que verifica se um número fornecido pelo usuário é primo ou não.

# Entrada do número
num = int(input("Digite um número para verificar se é primo: "))

# Verificação inicial
if num < 2:
    print(f"{num} não é um número primo.")
else:
    divisor = 2
    eh_primo = True

    # Loop para verificar divisores
    while divisor < num:
        if num % divisor == 0:  # Se for divisível por algum número, não é primo
            eh_primo = False
            break
        divisor += 1

    # Resultado
    if eh_primo:
        print(f"{num} é um número primo!")
    else:
        print(f"{num} não é um número primo.")