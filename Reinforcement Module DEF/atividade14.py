# Faça um descobridor de senhas de 4 digitos. mostre as tentativas (Enunciado é curto mais o problema é longo)

def descobridor_senha(senha_correta: str):
    for i in range(10000):
        tentativa = f'{i:4}'
        if tentativa == senha_correta:
            print(f'Senha encontrada: {tentativa}')
            return tentativa
    print('Senha não encontrada.')
    return None

senha = input('Digite a senha correta (4 dígitos): ')
descobridor_senha(senha)