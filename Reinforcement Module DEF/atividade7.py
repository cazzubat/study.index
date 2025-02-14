# - Crie uma função chamada media que receba três notas de um aluno e calcule e retorne a média delas.

def media(x, y, z):
    return (x + y + z) / 3

x1 = int(input('Insira um valor: '))
x2 = int(input('Insira um valor: '))
x3 = int(input('Insira um valor: '))

print(media(x1,x2,x3))