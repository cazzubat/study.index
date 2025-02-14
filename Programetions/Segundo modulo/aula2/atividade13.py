# 6 - Considere a seguinte lista:
livros = [
    "O Pequeno Príncipe",
    "Dom Quixote",
    "Cem Anos de Solidão",
    "1984",
    "Orgulho e Preconceito",
    "O Senhor dos Anéis",
    "Harry Potter e a Pedra Filosofal",
    "A Menina que Roubava Livros",
    "Crime e Castigo",
    "As Crônicas de Nárnia"
]

# Escreva um programa que filtra os livros a partir de uma letra fornecida como entrada pelo usuário. Por exemplo, caso o usuário digite a letra "a" todos os livros que contenham a letra "a" devem aparecer no resultado final.

# Entrada do usuário
escolha = input('Insira uma letra para filtrar os livros: ').lower()

# Loop para filtrar os livros
resultado = []
i = 0
while i < len(livros):
    if escolha in livros[i].lower():
        resultado.append(livros[i])
    i += 1

# Exibição do resultado
if resultado:
    print("Livros que contêm a letra '" + escolha + "':")
    for livro in resultado:
        print(livro)
else:
    print("Nenhum livro encontrado.")