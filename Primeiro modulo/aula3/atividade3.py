#03 - Crie um algoritmo em que o usuário informe seu gênero, sua altura e seu peso. Após, calcule e exiba na tela (terminal) o IMC do usuário.
nome = (input('insira seu nome: '))
genero = (input('insira seu genero: '))
altura = float(input('insira sua altura: '))
peso = float(input('insia seu peso: '))

calculo = altura + peso 

print(f'Nome: {nome}')
print(f'Genero: {genero}')
print(f'Altura: {altura}')
print(f'Peso: {peso}')

print(f'Calculo da Altura com Peso: {calculo}')
