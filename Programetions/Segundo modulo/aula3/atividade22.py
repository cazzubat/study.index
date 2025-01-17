# 3: Dado o dicionário do exercício anterior, altere a idade do aluno para 21.
# Imprima o dicionário após a modificação.

informaçoes = {
    'nome': 'Pedro',
    'idade': '18',
    'curso': 'Medicina'
}

del informaçoes['idade']
informaçoes['idade'] = 21
print(informaçoes['idade'])