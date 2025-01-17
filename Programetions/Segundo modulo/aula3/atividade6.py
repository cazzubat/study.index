# Exercício 6: Crie um programa que determina se um ano dado é bissexto. Um ano bissexto é divisível por 4, mas não é divisível por 100, a menos que também seja divisível por 400.

ano = int(input('Insira os dias de algum tipo dia de ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")