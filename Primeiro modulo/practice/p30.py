print('Exercicio Palindromo')

# Solicita a palavra do usuário
palavra = input("\nDigite uma palavra: ")

# Inicializa uma variável para a versão invertida
invertida = ''

# Usa o laço for para percorrer a palavra de trás para frente
for i in range(len(palavra) - 1, -1, -1):  # Começa do último índice e vai até o primeiro
    invertida += palavra[i]  # Adiciona o caractere invertido à variável 'invertida'

# Verifica se a palavra é um palíndromo
if palavra == invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
