# - Crie uma função eh_palindromo que recebe uma string e retorna True se ela for um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente EXEMPLO NATAN), e False caso contrário.


def palindromo(texto:str):
    return texto == texto [::-1]

palavra = input('Digite seu palindromo: ').strip().lower()

if palindromo(palavra):
    print('É palindromo')
else:
    print('Não é palindromo')