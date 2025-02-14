### **1. Função de Saudação Personalizada**
#**Objetivo:** Criar uma função que receba o nome de uma pessoa e retorne uma saudação personalizada.  
#**Instruções:**
#1. Defina uma função chamada `saudacao()`.
#2. A função deve receber um parâmetro chamado `nome`.
#3. A função deve retornar uma mensagem no formato: `"Olá, [nome]! Seja bem-vindo(a)!"`.  


def saudacao(name):
    return (f'Olá, {name}! Seja bem-vindo(a)!')

nome = input('Insira seu nome: ')
print(saudacao(nome))