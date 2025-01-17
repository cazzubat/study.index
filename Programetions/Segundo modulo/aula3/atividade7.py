# Exercício 7: Crie um programa que recebe como entrada a altura, profissão e nome de um individuo e: 
# Se o nome for Alice e a altura for 169, exiba a mensagem: "Suspeito encontrado"
# Se o nome for Douglas ou Rafael e a profissão começar com a letra C, exiba a mensagem: "Suspeito encontrado"
# Se o nome encontrado for Thiago e a profissão for 'Professor', exiba mensagem: Suspeito encontrado!

profissao =  input('Insira sua profissao: ').lower()
usuario = input ('Insira o seu nome: ').lower()
altura = input('Insira sua altura: ')

if usuario == 'alice' and altura == '169':
    print('Suspeito encontrado')
elif (usuario == 'douglas' or usuario == 'rafael') and profissao[0] == 'c':
    print('Suspeito encontrado')
elif usuario == 'thiago' and profissao == 'professor':
    print('Suspeito encontrado!')
else:
    print('Acesso concedido')