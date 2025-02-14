# 6.1 Crie uma função para filtrar alunos por nome.

nomes = [
    "Ana", "Bruno", "Carlos", "Diana", "Eduardo",
    "Fernanda", "Gabriel", "Hugo", "Isabela", "João",
    "Karina", "Lucas", "Mariana", "Nathan", "Olivia",
    "Paulo", "Rafael", "Sofia", "Tiago", "Vinícius"
]

print('Filtro de nomes')

letra = input('\nInsira uma letra: ').lower()

for i in nomes:
    if letra in i.lower():
        print(i)