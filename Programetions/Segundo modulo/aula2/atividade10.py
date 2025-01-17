estudantes = []

for estudante in range(3):
    nome = input(f'Digite o nome do estudante {estudante+1}: ')
    idade = int(input(f'Digite a idade do estudante {estudante+1}: '))
    nota = float(input(f'Digite a nota do estudante{estudante+1}: '))

    estudantes.append({
        'nome': nome,
        'idade': idade,
        'nota': nota
    })

    print('\nLista de Estudantes:')
for estudante in estudantes:
    print(estudante)