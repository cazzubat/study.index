from funções import *

tarefas = []

def menu():
    
    print('Escolha uma das opções abaixo:')
    print('1 - Adicionar tarefa')
    print('2 - Ver tarefas')
    print('3 - Remover tarefa')
    print('4 - sair')

    escolha = input('Escolha sua opção: ')

    if escolha == '1':
        print(f'você escolheu {escolha}')
        adicionar(tarefas) 

    elif escolha == '2':
        print(f'você escolheu {escolha}')
        print(tarefas)
    
    elif escolha == '3':
        print(f'você escolheu {escolha}')
        remover(tarefas)
    
    elif escolha == '4':
        print(f'você escolheu {escolha}')

    else:
        print('Escolha uma das opções válidas: ')

    if escolha != '4':
        return menu()
       
   
print('Seja bem vindo a lista de tarefas')
menu()
