# 6.2 Crie uma função para filtrar alunos por ano
alunos = [
    {"nome": "Ana", "ano": 1},
    {"nome": "Bruno", "ano": 2},
    {"nome": "Carlos", "ano": 3},
    {"nome": "Diana", "ano": 1},
    {"nome": "Eduardo", "ano": 2},
    {"nome": "Fernanda", "ano": 3},
    {"nome": "Gabriel", "ano": 1},
    {"nome": "Hugo", "ano": 2},
    {"nome": "Isabela", "ano": 3},
    {"nome": "João", "ano": 1},
    {"nome": "Karina", "ano": 2},
    {"nome": "Lucas", "ano": 3},
    {"nome": "Mariana", "ano": 1},
    {"nome": "Nathan", "ano": 2},
    {"nome": "Olivia", "ano": 3},
    {"nome": "Paulo", "ano": 1},
    {"nome": "Rafael", "ano": 2},
    {"nome": "Sofia", "ano": 3},
    {"nome": "Tiago", "ano": 1},
    {"nome": "Vinícius", "ano": 2}
]

try:
    ano_desejado = int(input('Insira o ano desejado: '))

    for aluno in alunos:
        if aluno["ano"] == ano_desejado:
            print(aluno["nome"])
except ValueError:
    print('Você inseriu um valor invalido.')