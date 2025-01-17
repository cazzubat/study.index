# - Crie uma função multiplicar_tupla que recebe uma tupla de números e retorna o produto de todos os elementos da tupla.

def multiplicar_tupla(tupla):
  somaresultado = 1
  for numero in tupla:
    somaresultado *= numero
  return somaresultado

print(multiplicar_tupla((4,5,6)))