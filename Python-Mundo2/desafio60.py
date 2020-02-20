'''
    desafio 60
	Faça um programa que leia um numero qualquer e leia seu fatorial
	ex: 5! = 5x4x3x2x1 = 120

utilizando o modulo math

from math import factorial
n = int(input('Digite um numero :'))
f = factorial(n)
print('Fatorial de {} é {}'.format(n, f))
'''

n = int(input('Digite um Numero para descobrir seu fatorial :'))
c = n
f = 1
print('\033[34mCalculando o Fatorial {}!\033[m = '.format(n), end='')
while c > 0:
       print('{}'.format(c),end= '')
       print(' X ' if c > 1 else ' = ', end='')
       f *= c
       c -= 1
print('\033[31m{}\033[m'.format(f))
        #print( 'Fatorando {} - {} X {} = {}'.format( n, n,fator, n * fator))
