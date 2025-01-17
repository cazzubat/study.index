# 39 - Desafio: Crie um algoritmo para calcular a velocidade de um veículo
# o calculo da velocidade é: velocidade distância/tempo
# os valores devem ser recebidos através de inputs.
# Caso valores não númericos sejam recebidos o deve ser exibida uma mensagem de erro:
# "Os valores inseridos não são números"
# Caso valores corretos sejam informados o algoritmo deve imprimir o valor da velocidade calculada.

try:
    distancia = float(input('Insira a distância do veículo (em km): '))
    tempo = float(input('Insira o tempo que ele vai percorrer (em horas): '))

    if tempo != 0:
        velocidade = distancia / tempo
        print(f'A velocidade calculada é {velocidade: .2} km/h')
    else:
        print('O tempo não pode ser zero.')

except ValueError:
    print('Os valores inseridos não são números.')