# 3 - Escreva um programa que solicite repetidamente ao usuário para digitar uma senha até que eles insiram a senha correta, escolhida por você.

senha_correta = '1234'

senha = input('Digite a senha correta: ')

while True:

    if senha == senha_correta:
        print('Acesso concedido.')
        break
    
    nova_tentiva = input('Insira a senha novamente: ')
    if nova_tentiva == senha_correta:
        print('Acesso concedido.')
        break
    