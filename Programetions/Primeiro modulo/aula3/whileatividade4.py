# 4 - Crie um algoritmo que recebe 5 nomes e imprime no terminal os nomes que se iniciem com uma letra à sua escolha:
# Ex: 'Ana', 'Julia', 'Pedro', 'Amanda', 'Bruno' , letra = "A", a saída no terminal dever ser:
# Ana
# Amanda
# Obs: Se atentem para o uso de letras maiúsculas ou minúsculas

letra = input('Insira a letra: ')

nomes = ['Ana', 'Julia', 'Pedro', 'Thayna', 'Gabriela', 'Luiz']
n = 0

while n < len(nomes):
    if nomes[n][0].lower() == letra.lower():
        print(nomes[n])
    n += 1