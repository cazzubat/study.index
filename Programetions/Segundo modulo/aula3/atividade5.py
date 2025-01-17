# Exercício 5: Escreva um programa que solicita ao usuário uma senha. Se a senha for "12345", imprima "Acesso concedido"; caso contrário, imprima "Acesso negado".

senha_correta = '12345'

senha = input('Insira sua senha: ')

if senha == senha_correta:
    print('Acesso concedido.')
else:
    print('Acesso negado.')