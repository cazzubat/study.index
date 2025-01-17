# 1  - Crie um algoritmo em que o usuário informe uma frase qualquer e exiba a frase na tela (terminal) quando executado.
frase = input('insira uma frase: ')

# 2  - Crie um algoritmo em que o usuário informe o nome completo e exiba o nome completo na tela (terminal) quando executado.
nome = input('insira seu nome completo: ')
print(nome)

# 3  - Crie um algoritmo em que o usuário informe a idade e exiba a idade na tela (terminal) quando executado.
idade = input('insira sua idade: ')
print(idade)

# 4  - Crie um algoritmo em que o usuário informe dois números inteiros (n1 e n2) e exiba os números na tela (terminal) quando executado.
number1 = input('insira o primeiro numero: ')
number2 = input ('insira o segundo numero: ')
print(number1, number2)

# 5  - Crie um algoritmo em que o usuário informe dois números inteiros (n1 e n2) e exiba a soma dos números na tela (terminal) quando executado.
number1 = int(input('insira o primeiro numero: '))
number2 = int(input('insira o segundo numero: '))
print(number1 + number2)

# 6  - Crie um algoritmo em que o usuário informe dois números inteiros (x1 e x2) e exiba a diferença dos números na tela (terminal) quando executado.
number1 = int(input('insira o primeiro numero: '))
number2 = int(input('insira o segundo numero: '))
print(number1 - number2)

# 7  - Crie um algoritmo em que o usuário informe dois números inteiros (a1 e a2) e exiba o produto dos números na tela (terminal) quando executado.
number1 = int(input('insira o primeiro numero: '))
number2 = int(input('insira o segundo numero: '))
print(number1 * number2)

# 8  - Crie um algoritmo em que o usuário informe dois números inteiros (x e y) e exiba o quociente dos números na tela (terminal) quando executado.
number1 = int(input('insira o primeiro numero: '))
number2 = int(input('insira o segundo numero: '))
print(number1 / number2)

# 9  - Crie um algoritmo em que o usuário informe quatro notas (n1, n2, n3 e n4). Após, calcule a média aritmética e exiba a média na tela (terminal) quando executado.
number1 = int(input('insira o primeiro numero: '))
number2 = int(input('insira o segundo numero: '))
number3 = int(input('insira o terceiro numero: '))
number4 = int(input('insira o quarto numero: '))

soma = number1 + number2 + number3 + number4

print(soma / 4 )

# 10 - Primeiro Desafio
email = input('inserir email: ')
senha = input('inserir senha: ')
if email == 'gabrielvianna@gmail.com' and senha == 'bengalalistrada1234':
    print('acesso aprovado')
else:
    print('acesso negado')

# 11 - Segundo Desafio
nome = input('insira seu nome: ')
idade = input('insira sua idade: ')
fruta_favorita = input('insira sua fruta favorita: ')
aluno = input('você é aluno da infinity? ')

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Fruta Favorita: {fruta_favorita}')
print(f'Aluno da Infinity: {aluno}')