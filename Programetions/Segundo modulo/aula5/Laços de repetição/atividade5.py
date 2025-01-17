# 5 - Crie um algoritmo aque receba um número de usuário e informe a soma de todos os números anteriores ao valor informado:
# Ex: 3 , o resultado devera ser: 1 + 2 + 3 = 6 , então no terminal deverá ser exibido o número 6.

numero = int(input("Digite um número inteiro: "))
soma = sum(range(1, numero + 1))  # Calcula a soma de 1 até o número informado
operacao = " + ".join(str(i) for i in range(1, numero + 1))  # Cria a string da operação
print(f"{operacao} = {soma}")
