numero1 = int(input("Digite o número inicial do intervalo: "))
numero2 = int(input("Digite o número final do intervalo: "))

stock = 0

for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        stock += numero

if stock == 0:
    print("Não há números pares no intervalo.")
else:
    print(f"A soma dos números pares no intervalo é: {stock}")
