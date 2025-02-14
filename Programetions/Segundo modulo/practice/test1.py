numero1 = int(input('Insira o primeiro numero: '))
numero2 = int(input('Insira o segundo numero: '))
numero3 = int(input('Insira o terceiro numero: '))

def maior_numero():
    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero2
    else:
        return numero3
    
print(maior_numero())