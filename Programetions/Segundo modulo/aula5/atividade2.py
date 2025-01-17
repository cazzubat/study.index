# 32 - Crie um algoritmo que ao ser executado verifica uma variável "chuva" e 
# se for verdadeiro exibe a mensagem: "Leve um guarda chuva"
# e se for falso exiba a mensagem: "Olha que dia bonito, nem precisa levar guarda-chuva"

import random

clima = ['sol', 'chuva']

clima_aleatorio = random.choice(clima)

if clima_aleatorio == 'chuva':
    print('Olha que dia bonito, nem precisa levar guarda-chuva')
else:
    print('Leve um guarda chuva')