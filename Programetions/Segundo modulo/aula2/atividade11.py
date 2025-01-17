lista = [{'nome': 'pedro', 'idade': 10, 'nota': 2.0},
{'nome': 'gabriel', 'idade': 203, 'nota': 3.0},
{'nome': 'julio', 'idade': 30, 'nota': 3.0},
{'nome': 'breno', 'idade': 30, 'nota': 3.0},
{'nome': 'ana', 'idade': 30, 'nota': 3.0},
{'nome': 'antonia', 'idade': 30, 'nota': 3.0},
{'nome': 'angelica', 'idade': 30, 'nota': 3.0},
]

for aluno in lista:
    if aluno.get('nome')[0] == 'a' and aluno.get('nome')[1] == 'n':
        print(aluno.get('nome'))