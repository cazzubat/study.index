# - Crie uma função chamada saudar que recebe o nome de uma pessoa como parâmetro e retorna uma saudação personalizada (ex: "Olá, [nome]!").

nome = input('Insire seu nome: ')

def saudacao(nome):
    return (f'Olá, {nome}')

print(saudacao(nome))