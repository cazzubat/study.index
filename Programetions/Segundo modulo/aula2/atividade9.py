# 2- Crie um algoritmo que recebe um número, faz o somatório de todos os valores até este número e exibe o somatório final no terminal.  Ex: n=3  o resutlado deverá ser 6 (1 + 2 + 3)

n = int(input('Insira um número: '))

contador = 1
soma = 0

while n > contador:
    soma += contador
    contador += 1

print(f'o somatório de todos os números até {n} é: {soma}')