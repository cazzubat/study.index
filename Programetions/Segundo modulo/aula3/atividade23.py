# 4: Adicione a chave "curso" com o valor "Engenharia" a um dicionário vazio.
# Imprima o dicionário.

informaçoes = {
    'nome': 'Pedro',
    'idade': '18',
    'curso': 'Medicina'
}

del informaçoes['curso']
informaçoes['curso'] = 'Engenharia'
print(informaçoes['curso'])