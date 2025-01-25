import random

print('Bem-vindo ao jogo de Pedra, Papel e Tesoura!')
print('Regra: No jogo de Pedra, Papel e Tesoura, Pedra quebra Tesoura, Tesoura corta Papel, Papel embrulha Pedra, e escolhas iguais resultam em empate.')


def jogo():
    lista = ['pedra', 'papel', 'tesoura']
    ponto_humano = 0
    ponto_maquina = 0

    
    escolha = input('\nEscolha uma opção (pedra, papel, tesoura): ').lower()
        
    # Escolha
    if escolha in lista:
        maquina = random.choice(lista)
    else:
        print('Digite uma resposta válida.')
        return jogo()

    # Verificação Humano vitória
    if (maquina == 'papel' and escolha == 'tesoura') or \
        (maquina == 'tesoura' and escolha == 'pedra') or \
        (maquina == 'pedra' and escolha == 'papel'):
        ponto_humano += 1
        print(f'Você marcou {ponto_humano} pontos.')

    # Verificação Máquina vitória
    elif (maquina == 'tesoura' and escolha == 'papel') or \
        (maquina == 'pedra' and escolha == 'tesoura') or \
        (maquina == 'papel' and escolha == 'pedra'):
        ponto_maquina += 1
        print(f'Você perdeu! A máquina escolheu {maquina} e agora tem {ponto_maquina} pontos no placar.')

    # Empate
    else:
        print('Empate!')
    
    # Saída
    continuar = input('Deseja continuar? (S/N): ').lower()
    if continuar == 'n':
        print('Obrigado por jogar o jogo.')
        return ponto_humano, ponto_maquina
    
    elif continuar != 's':
        print('Digite uma resposta válida na próxima vez.')
        return jogo()
        
    return ponto_humano, ponto_maquina

ponto_humano, ponto_maquina = jogo()

def placar(ponto_humano, ponto_maquina):
    print(f'\nO placar atual é: Você {ponto_humano} x {ponto_maquina} Máquina')

placar(ponto_humano,ponto_maquina)
