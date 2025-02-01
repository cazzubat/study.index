
def adicionar(lista:list):
    add_tarefa = input('Insira uma tarefa: ').lower().strip()
    lista.append(add_tarefa)

def remover(lista:list):
    lista.pop()