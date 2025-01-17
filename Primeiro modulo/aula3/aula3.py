#Exemplo While (Complexo):

senhas_validas = ["1234" , "4321", "1111", "2222"]

print(senhas_validas[0]) # imprimir 1234, que é o primeiro item da lista;

n = 0
print(len(senhas_validas)) 
senha_digitada = input('Digite sua senha: ')

while n < len(senhas_validas):
    if senha_digitada == senhas_validas[n]:
        print('Acesso concedido')
        break
    else:
        senha_digitada = input('Senha incorreta, tente novamente: ')
    n = n + 1
    if(n == 4):
        print('Acesso Bloqueado, numero de tentativas máximas esgotado')

#Exemplo mais gentil do laço de repetição while:
# Contar quantas letras tem a palavra que o usuário digitou:

palavra = input('Digite uma palavra: ')

contador = 0

#Estrutura do sintática do while:
while contador < len(palavra):
    contador += 1
    print(contador)

print(f'A palavra tem {contador} letras')


print('Acesso Bloqueado, numero de tentativas máximas esgotado')