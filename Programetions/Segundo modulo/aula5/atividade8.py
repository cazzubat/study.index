# 37 - Crie um algoritmo que ao ser executado recebe a velocidade de dois veículos em km/h
# e exibe no terminal qual dos veículos está se deslocando mais rápido.
# - Se algum dos veículos estiver acima de 80km/h deve ser exibida a mensagem: "veículo <número> está acima da velocidade permitida"
# - Se algum dos veículos estiver a 0km/h deve ser exibida a mensagem: "veículo <número> não está em movimento"

velocidade1 = int(input('Insira a velocidade do primeiro veículo: '))
velocidade2 = int(input('Insira a velocidade do segundo veículo: '))

# Comparação de velocidades
if velocidade1 > velocidade2:
    print('A velocidade do primeiro veículo é maior que a do segundo')
else:
    print('A velocidade do segundo veículo é maior que a do primeiro')

# Verificação de velocidade permitida
if velocidade1 > 80:
    print('A velocidade do primeiro veículo está acima da velocidade permitida')
elif velocidade2 > 80:
    print('A velocidade do segundo veículo está acima da velocidade permitida')

# Verificação de veículos parados
if velocidade1 == 0:
    print('O primeiro veículo está parado')
elif velocidade2 == 0:
    print('O segundo veículo está parado')