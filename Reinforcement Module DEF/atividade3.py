### **3. Função para Verificar se um Número é Par**
#**Objetivo:** Criar uma função que receba um número e retorne se ele é par ou ímpar.  
#**Instruções:**
#1. Defina uma função chamada `verificar_par()`.
#2. A função deve receber um número como parâmetro.
#3. A função deve retornar `"Par"` se o número for par e `"Ímpar"` se não for.

def verificar_par(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

verificação = int(input('Insira um numero: '))
print(verificar_par(verificação))