# - Crie uma função chamada contagem_regressiva que recebe um número n e imprime os números de n até 1, em contagem regressiva.

def contagem_regressiva(x:int):
    for i in range(x,0,-1):
        print(i)

numero = int(input('Insira um numero: '))
(contagem_regressiva(numero))