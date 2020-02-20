#  refaça o desafio 35 dos triangulos,acrescentando o recurso de mostrar que tipo de triangulo será formado

#  equilátero: todos os lados iguais
#  isoceles: dois lados iguais
#  escaleno: todos os lados diferentes

r1 = float(input('Primeiro segmento :'))
r2 = float(input('Segundo segmento :'))
r3 = float(input('Terceiro segmento :'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34msegmento forma um triangulo ', end="")
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOCELES!')
else:
    print('Esses segmentos nao formam um triangulo')
