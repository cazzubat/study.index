# - Crie uma função desconto que receba o preço de um produto e um percentual de desconto (opcional, com valor padrão de 10%). A função deve retornar o preço com o desconto aplicado.

def desconto(num):
    return  num - (num * 0.10) 

number = float(input('Insira um valor: '))

print(f'Após o desconto, sua compra ficou no valor de: {desconto(number)}')