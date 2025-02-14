### **2. Função para Calcular o Dobro de um Número**
#**Objetivo:** Criar uma função que receba um número e retorne o dobro desse número.  
#**Instruções:**
#1. Defina uma função chamada `dobro()`.
#2. A função deve receber um número como parâmetro.
#3. A função deve retornar o dobro do número.


def dobro(numero):
    return numero + numero

numero1 = int(input('Insira um numero: '))
print(dobro(numero1))