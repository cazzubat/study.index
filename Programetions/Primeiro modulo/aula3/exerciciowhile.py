#Exercícios WHILE:

# 0 : Através do exemplo do contador de letras, crie um algoritmo que exiba cada letra de uma palavra digitada pelo usuário;


# 1 - Crie um algoritmo que receba um número e imprima no terminal todos os valores em ordem crescente até o valor do número informado.
# Ex: n = 5, a saída no terminal devera ser:
# 1
# 2
# 3
# 4
# 5



# 2 - Crie um algoritmo que receba um número e imprima no terminal todos os valores em ordem decrescente até o valor do número informado.
# Ex: n = 6, a saída no terminal devera ser:
# 6
# 5
# 4
# 3
# 2
# 1



# 3 - Crie um algoritmo que ao receber uma palavra conte o número de letras dessa palavra e imprima esse valor no terminal.


# 4 - Crie um algoritmo que recebe 5 nomes e imprime no terminal os nomes que se iniciem com uma letra à sua escolha:
# Ex: 'Ana', 'Julia', 'Pedro', 'Amanda', 'Bruno' , letra = "A", a saída no terminal dever ser:
# Ana
# Amanda
# Obs: Se atentem para o uso de letras maiúsculas ou minúsculas

# 5 - Crie um algoritmo aque receba um número de usuário e informe a soma de todos os números anteriores ao valor informado:
# Ex: 3 , o resultado devera ser: 1 + 2 + 3 = 6 , então no terminal deverá ser exibido o número 6.



# 7 - Crie um algoritmo que ao receber um número calcule a tabuada deste número até 10 e exiba cada uma das multiplicações no terminal
# Ex: numero = 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

# 9 - Crie um algoritmo para que o usuário possa selecionar uma das três opções: "pedra", "papel", "tesoura"
# imprima a opção escolhida pelo usuário. Caso o usuário escolha uma opção inválida exiba a mensagem "Escolha inválida, tente novamente"
# O algoritmo só para sua execução quando o usuário escolher entre uma das opções válidas, exibindo qual opção foi escolhida.

# 6 - Crie um algoritmo que ao receber uma palavra a reescreve de trás para frente.


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


#Exemplo mais gentil de While:
# Contar quantas letras tem a palavra que o usuário digitou:

palavra = input('Digite uma palavra')

contador = 0

#Estrutura do sintática do while:
while contador < len(palavra):
    contador += 1
    print(contador)

print(f'A palavra tem {contador} letras')
