# 6.3 Crie uma função para filtrar alunos por desempenho em uma materia específica.

alunos = {
    "Ana": {"nome": "Ana", "ano": 1, "notas": {"Matemática": 8, "Português": 7, "Ciências": 9}},
    "Bruno": {"nome": "Bruno", "ano": 2, "notas": {"Matemática": 6, "Português": 8, "Ciências": 7}},
    "Carlos": {"nome": "Carlos", "ano": 3, "notas": {"Matemática": 9, "Português": 7, "Ciências": 8}},
    "Diana": {"nome": "Diana", "ano": 1, "notas": {"Matemática": 7, "Português": 9, "Ciências": 6}},
    "Eduardo": {"nome": "Eduardo", "ano": 2, "notas": {"Matemática": 8, "Português": 6, "Ciências": 7}},
    "Fernanda": {"nome": "Fernanda", "ano": 3, "notas": {"Matemática": 9, "Português": 8, "Ciências": 6}},
    "Gabriel": {"nome": "Gabriel", "ano": 1, "notas": {"Matemática": 6, "Português": 7, "Ciências": 9}},
    "Hugo": {"nome": "Hugo", "ano": 2, "notas": {"Matemática": 7, "Português": 9, "Ciências": 8}},
    "Isabela": {"nome": "Isabela", "ano": 3, "notas": {"Matemática": 8, "Português": 7, "Ciências": 9}},
    "João": {"nome": "João", "ano": 1, "notas": {"Matemática": 9, "Português": 6, "Ciências": 8}},
    "Karina": {"nome": "Karina", "ano": 2, "notas": {"Matemática": 8, "Português": 9, "Ciências": 7}},
    "Lucas": {"nome": "Lucas", "ano": 3, "notas": {"Matemática": 7, "Português": 8, "Ciências": 9}},
    "Mariana": {"nome": "Mariana", "ano": 1, "notas": {"Matemática": 6, "Português": 9, "Ciências": 7}},
    "Nathan": {"nome": "Nathan", "ano": 2, "notas": {"Matemática": 9, "Português": 7, "Ciências": 6}},
    "Olivia": {"nome": "Olivia", "ano": 3, "notas": {"Matemática": 8, "Português": 6, "Ciências": 9}},
    "Paulo": {"nome": "Paulo", "ano": 1, "notas": {"Matemática": 7, "Português": 8, "Ciências": 9}},
    "Rafael": {"nome": "Rafael", "ano": 2, "notas": {"Matemática": 9, "Português": 6, "Ciências": 7}},
    "Sofia": {"nome": "Sofia", "ano": 3, "notas": {"Matemática": 7, "Português": 9, "Ciências": 8}},
    "Tiago": {"nome": "Tiago", "ano": 1, "notas": {"Matemática": 8, "Português": 7, "Ciências": 6}},
    "Vinícius": {"nome": "Vinícius", "ano": 2, "notas": {"Matemática": 6, "Português": 8, "Ciências": 9}}
}


materia_desejada = input('Insira a materia desejada: ').capitalize()

for aluno in alunos:
    if materia_desejada in alunos[aluno]["notas"]:
        print(f"{aluno}: {alunos[aluno]['notas'][materia_desejada]}")  