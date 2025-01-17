# - Crie uma função chamada contagem_regressiva que recebe um número n e imprime os números de n até 1, em contagem regressiva.
numero = int(input('Insira um numero inteiro: '))

def contagem_regressiva(numero):
    for percorrer in range(numero, 0, -1):
        print(percorrer)

contagem_regressiva(numero)