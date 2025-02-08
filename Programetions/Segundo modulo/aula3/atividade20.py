# 5: Verifique se a chave "curso" existe em um dicionário.
# Imprima uma mensagem de acordo com o resultado.

informaçoes = {
    'nome': 'Pedro',
    'idade': '18',
    'curso': None
}

del informaçoes['idade']
informaçoes['idade'] = 21
print(informaçoes['idade'])

verificacao = informaçoes.get('curso')

if verificacao is None:
    print('A chave não foi encontrada')
else:
    print(verificacao)
