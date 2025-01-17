# 1 - Crie um algoritmo que receba um número e imprima no terminal todos os valores em ordem crescente até o valor do número informado.
# Ex: n = 5, a saída no terminal devera ser:
# 1
# 2
# 3
# 4
# 5

numero = int(input('insira um numéro até aonde você quer contar: '))
contador = 0

while numero > contador:
    contador += 1
    print(contador)