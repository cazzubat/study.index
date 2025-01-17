print('Adivinhação de número')

nm = int(input('Insira o número: '))
n = 50

if nm < 50:
    print('O número que você colocou é menor.')
elif nm > 50:
    print('O número que você colocou é maior.')
else:
    print('Você acertou.')