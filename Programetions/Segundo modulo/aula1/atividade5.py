estudante = {
    'nome': 'Gabriel',
    'idade': 17,
    'cursos': ['informatica', 'ingles', 'espanhol', 'administração']
}

estudante['matricula'] = True

estudante['idade'] = 22

del estudante['cursos']

if 'cursos' in estudante:
    print(estudante['cursos'])
else:
    print("A chave 'cursos' foi removida.")