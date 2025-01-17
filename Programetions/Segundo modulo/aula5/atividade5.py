# 35 - Crie um algoritmo que recebe três números e compare cada desses números e imprima: 
# Para o menor número a mensagem: "<numero1> é o menor entre os números fornecidos"
# Para o número intermediário: "<numero2> está entre <numero2> e <numero3>"
# Para o maior número: "<numero3> é o maior entre os números"

numero1 = int(input('Insira o primeiro valor: '))
numero2 = int(input('Insira o segundo valor: '))
numero3 = int(input('Insira o terceiro valor: '))

if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
    if numero2 <= numero3:
        intermediario = numero2
        maior = numero3
    else:
        intermediario = numero3
        maior = numero2
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
    if numero1 <= numero3:
        intermediario = numero1
        maior = numero3
    else:
        intermediario = numero3
        maior = numero1
else:
    menor = numero3
    if numero1 <= numero2:
        intermediario = numero1
        maior = numero2
    else:
        intermediario = numero2
        maior = numero1

print(f'{menor} é o menor entre os números fornecidos')
print(f'{intermediario} está entre {menor} e {maior}')
print(f'{maior} é o maior entre os números fornecidos')
