def concatenar():
    lista = []  
    while True:
        entrada = input('Insira um caractere: ')  
        lista.append(entrada)  
        
        saida = input('Deseja continuar? S/N: ').lower()
        
        if saida == 'n':
            break  
        elif saida != 's':
            print('Resposta inválida. Por favor, insira "S" para continuar ou "N" para parar.')
    
    resultado = ''.join(lista)
    print(f'Caractere concatenado: {resultado}')
    
concatenar()
