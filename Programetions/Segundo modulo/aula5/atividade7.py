# 38 - Crie um algoritmo que ao ser executado recebe uma frase,
# e verifica se uma letra escolhida por você está presente na frase
# caso a frase contenha a letra escolhida deve ser exibida a mensagem "A letra <letra> está presente na frase"
# caso contrário deve ser exibida a frase "A letra <letra> não está contida na frase"

frase = input('Insira uma palavra: ')

letra_a = 'a'

if letra_a in frase:
    print('A letra A está presente na frase')
else:
    print('A letra A não está presente na frase')