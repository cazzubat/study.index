# 31 - Crie um algoritmo que ao ser executado que verifica se um número é par ou ímpar 
# e exibe a mensagem "ímpar" se o número for ímpar e "par" se o número for par.

# Um número é par quando o resto da divisão por 2 é zero.
# Se o módulo de n % 2 for 0 este número é par.

print('Verificação se é par')

numero = int(input('\nInsira o numero: '))

if numero % 2 == 0:
    print('\nO numero é par')
else:
    print('\nO numero é impar')