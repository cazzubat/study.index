# 4 - Crie um algoritmo que recebe 5 nomes e imprime no terminal todos aqueles iniciados em uma letra à sua escolha:
# Ex: 'Ana', 'Julia', 'Pedro', 'Amanda' , letra = "A", a saída no terminal dever ser:
# Ana
# Amanda
# Obs: Se atentem para o uso de letras maiúsculas ou minúsculas

lista = []

for i in range(5):
    nome = input(f'Insira o {i + 1}º nome: ').lower()
    lista.append(nome)
    print(f'O nome "{nome}" foi adicionado à lista.')

print("\nNomes que começam com 'a':")
for nome in lista:
    if nome.lower().startswith('a'):
        print(nome)