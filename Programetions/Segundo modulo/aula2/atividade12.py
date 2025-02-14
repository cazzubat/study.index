vogais = ['a', 'e', 'i', 'o', 'u']

palavra = input('Insira uma palavra: ').lower()  # Converte para minúsculas
vogal = 0
i = 0  # Índice para percorrer os caracteres da palavra

# Usa um loop while para iterar sobre cada caractere da palavra
while i < len(palavra):
    if palavra[i] in vogais:  # Verifica se o caractere atual é uma vogal
        vogal += 1
    i += 1  # Incrementa o índice para avançar para o próximo caractere

print(f'A palavra "{palavra}" contém {vogal} vogais.')