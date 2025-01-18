import random

print('Bem-vindo ao jogo de Pedra, Papel e Tesoura!')
print('Regra: No jogo de Pedra, Papel e Tesoura, Pedra quebra Tesoura, Tesoura corta Papel, Papel embrulha Pedra, e escolhas iguais resultam em empate.')


lista = ['papel','tesoura', 'pedra']
placar = []
ponto_humano = 0
ponto_maquina = 0

while True:
    escolha = input('\nEscolha uma opção (pedra,papel,tesoura): ').lower()
    #Escolha
    if escolha in lista:
        maquina = random.choice(lista)
    
    else:
        print('Digite uma resposta valida.')
        continue

#Verificação Humano vitoria
    if  (maquina == 'papel' and escolha == 'tesoura') or \
        (maquina == 'tesoura' and escolha == 'pedra') or \
        (maquina == 'pedra' and escolha == 'papel'):
        ponto_humano += 1
        print(f'Você marcou {ponto_humano}')

#Verificação Maquina Vitoria
    elif (maquina == 'tesoura' and escolha == 'papel') or \
         (maquina == 'pedra' and escolha == 'tesoura') or \
         (maquina == 'papel' and escolha == 'pedra'):
        ponto_maquina += 1
        print(f'Você perdeu! A máquina escolheu {maquina} e agora tem {ponto_maquina} pontos no placar.')


#Empate
    else:
        print('Empate!')
    
#Saida    
    continuar = input('Deseja continuar? (S/N): ').lower()
    if continuar == 'n':
        break
    elif continuar != 's':
        print('Digite uma resposta válida.')

def placar():
    print(f'\nO placar atual é: Você {ponto_humano} x {ponto_maquina} Máquina')

placar()
