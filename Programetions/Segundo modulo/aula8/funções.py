def adicionar(lista:list):
    add_tarefa = input('Insira uma tarefa: ').lower().strip()
    lista.append(add_tarefa)

def remover(lista:list):
    lista.pop()

def alterar(lista:list):
   try:
       escolha = int(input('Escolha a posição da tarefa que deseja alterar: '))


       lista[escolha - 1] = input('Digite um novo valor: ')
   except ValueError:
       print('Vocẽ inseriu um valor invalido.')
