# 10 - Crie um algorimto que ao receber uma lista de números imprime o somatório dos números da lista.


lista = []
vezes = 0
    
while True:
    vezes += 1
    numero = int(input(f'Insira um número {vezes}º lista: '))
    lista.append(numero)
    resposta = input('Deseja continuar? (S/N): ')
    if resposta.upper() == 'N':
        break
    elif resposta.upper() != 'S':
        print('Opção inválida, tente novamente!')

soma = sum(lista)
print(f'O somatório da lista é: {soma}')
