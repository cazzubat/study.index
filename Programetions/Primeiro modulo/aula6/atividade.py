print('Menu de lista de Tarefas.')
print('Quando quiser que o programa pare de executar digite. (sair)')

tarefas = []
senha_valida = 'pedro1234'
senha = input('\nDigite a senha: ')

if senha == senha_valida:
    print('Acesso permitido.')
else:
    print('Acesso negado.')

certo = senha == senha_valida

if certo: 
    print('\nBom dia! Dê uma olhada nas nossas tarefas. ')

while certo:
    print('\n1- Adicionar tarefa')
    print('2- Concluir tarefa')
    print('3- Ver tarefa')
    
    sair = input('\nCaso nada de te interesse digite (sair), caso ao contrario só digite (continuar): ')
    if sair == 'sair':
        print('Tchau, muito obrigado por utilizar o nosso serviços.')
        break

    elif sair == 'continuar':
        print('\nOk, iremos mostrar a lista denovo para que você escolhe alguma delas.')
        print('\n1- Adicionar tarefa')
        print('2- Concluir tarefa')
        print('3- Ver tarefa')
        
        escolha = input('\nEscolha alguma das materias para interagir(digite o número do ínicio delas): ')
        if escolha == '1':
            tarefa = input('Adicione uma tarefa: ').lower().strip()
            tarefas.append(tarefa)
            print(f'\nFoi adiciona a tarefas: {tarefas}')
        
        elif escolha == '2':
            print(f'\nEscolha a tarefa que você deseja concluir: {tarefas}')
            escolha_tarefa = input('Escolha a tarefa: ').lower().strip()
            if escolha_tarefa in tarefas:
                tarefas.remove(escolha_tarefa)
        
        elif escolha == '3':
            print(f'\nA exatamente essas tarefas no sistema: {tarefas}')
                        

    else:
        print('Sua resposta não é valida.')
        break
    




    

