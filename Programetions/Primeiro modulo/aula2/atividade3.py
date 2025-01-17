pergunta1 = int(input('Qual é sua idade:'))
pergunta2 = input('Vc tem carteira de habilitação:')

if pergunta1 >=18 and pergunta2 == "sim":
    print('Você tem permissão para dirigir')
elif pergunta1 <=18:
    print('Você não tem permissão para dirigir')
else:
    print('Você não tem permissão para dirigir')
