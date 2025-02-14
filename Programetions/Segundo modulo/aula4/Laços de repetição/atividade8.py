# 8 - Crie um algoritmo que receba 7 nomes de usuário e ao final imprima cada um dos nomes em ordem alfabética.

# Lista para armazenar os nomes dos usuários
lista_user = []

# Loop para receber 7 nomes de usuário
for i in range(7):
    nome = input(f"Digite o nome do usuário {i+1}: ")  # Solicita o nome do usuário
    lista_user.append(nome)  # Adiciona o nome à lista
    print(f'O usuário {nome} foi adicionado.')  # Confirma a adição do nome

# Ordena a lista de nomes e imprime cada um
print("\nNomes em ordem alfabética:")
for nome in sorted(lista_user):
    print(nome)  # Imprime o nome
