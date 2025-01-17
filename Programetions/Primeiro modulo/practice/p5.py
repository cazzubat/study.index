print('Sistema de notas')

nota = float(input('Infome sua nota: '))

if nota >= 7.0:
    print('Você foi aprovado.')
elif nota >= 5:
    print('Você está de recuperação.')
else:
    print('Você foi reprovado.')