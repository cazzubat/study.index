while True: 
    nome = input("Digite seu nome: ")
    pergunta = input('Quer continuar? (sim/não)').lower()
    if pergunta in ['n','nao','não'] :
        print("Acabou")
        break
    altura = float(input("Digite sua altura: "))
    if pergunta == True:
        altura == 1.89
    elif altura > 1.89:
        print('Você é mais alto que o Gabriel')
    else:
        print('Gabriel é mais alto, ele tem 1.89')
        break
