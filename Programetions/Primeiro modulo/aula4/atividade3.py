fatorial = int(input("Insira o número fatorial: "))
resultado = 1

while fatorial > 1:
    resultado *= fatorial
    fatorial -= 1
print("O fatorial é:", resultado)