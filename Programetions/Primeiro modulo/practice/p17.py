print('Calculadora simples')
print('Caso queira sair do programa digite "sair"')

while True:
    numero1 = float(input('\nPrimeiro número: '))
    numero2= float(input('Segundo número: '))

    pergunta = input('\nQual tipo de conta você quer fazer? (soma, subtração, multiplicação, divisão): ').lower().strip()
    
    if pergunta == 'sair':
        print('Você encerrou o codigo.')
        break

    if pergunta == 'soma':
        print(f'\n{numero1} + {numero1} = {numero1 + numero2}')
    elif pergunta == 'subtração':
        print(f'\n{numero1} - {numero2} = {numero1 - numero2}')
    elif pergunta == 'multiplicação':
        print(f'\n{numero1} x {numero2} = {numero1 * numero2}')
    elif pergunta == 'divisão':
        print(f'\n{numero1} / {numero2} = {numero1 / numero2:.2f}')
        continue
    else:
        print('Digite uma resposta valida.')