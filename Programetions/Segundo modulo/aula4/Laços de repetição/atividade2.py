# 2 - Crie um algoritmo que receba um número e imprima no terminal todos os valores em ordem decrescente até o valor do número informado.
# Ex: n = 6, a saída no terminal devera ser:
# 6
# 5
# 4
# 3
# 2
# 1

numero = int(input("Digite um número: "))

for contador in range(numero, 0, -1):
    print (contador)