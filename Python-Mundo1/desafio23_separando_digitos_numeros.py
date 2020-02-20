#faça um programa que leia de o a 9999 e mostre na tela
#cada um digito separados
#exemplo
#digite um numero: 1834
#unidades: 4, dezena3, centena 8, milhar 1
num = int(input('Digite um numero :'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {} '.format(c))
print('Milhar {}'.format(m))