nota1 = float(input('nota matematica:'))
nota2 = float(input('nota geografia:'))

print('a media é 6 pontos em cada materia')

if nota1 >=6 and nota2 >=6:
    print('as notas estão na media')
elif nota1 <= 6 and nota2 >=6:
    print('apenas a nota do matematica  está abaixo da media')
elif nota1 >=6 and nota2 <=6:
    print('apenas a nota do geografia está abaixo da media')
else:
    print('suas notas estão a baixo da media')
