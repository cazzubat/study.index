# 6 - Crie um algoritmo em que o usuário informe um número qualquer. Após, informe se esse número é múltiplo de 5.
number = float(input('insira um numero: '))

if number % 5 == 0:
    print('é mutiplo por 5')
else:  
    print('não é mutiplo por 5')