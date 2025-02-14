# 33 - Crie um algoritmo que ao ser executado verifica: Se está ensolarado e se é fim de semana, 
# caso seja fim de semana E esteja ensolarado exiba a mensagem: "Bora pra praia de mineiro?" 
# senão exiba a mensagem: "Bora ver um trem no Netflix?"

import random

clima = ['sol', 'chuva']

clima_aleatorio = random.choice(clima)

if clima_aleatorio == 'chuva':
    print("Bora pra praia de mineiro?")
else:
    print("Bora ver um trem no Netflix?")