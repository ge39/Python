#desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
print('-='*20)
print('analisador de triangulos')
r1 = float(input('primero segmento :'))
r2 = float(input('segundo seguimento :'))
r3 = float(input('terceiro segmento :'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triangulos')
else:
    print("Os segmentos acima não podem formar triangulo")


