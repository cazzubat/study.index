# 5 - Crie um algoritmo aque receba um número de usuário e informe a soma de todos os números anteriores ao valor informado:
# Ex: 3 , o resultado devera ser: 1 + 2 + 3 = 6 , então no terminal deverá ser exibido o número 6.

numero = int(input('insira um numero: '))

n = 0
resultado = 0

while n <= numero:
    resultado += n
    n += 1
print(resultado)