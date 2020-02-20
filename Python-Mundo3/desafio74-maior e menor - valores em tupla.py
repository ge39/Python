'''
    Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla
    Depois disso, mostre a listagem de numeros gerados e tambem indique
    o menor eo maior valor que estão na tupla
'''
n = 0
from random import randint

numeros = (randint(1, 15), randint(10, 15), randint(10, 15), randint(10, 15), randint(10, 15))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=" ")
print(f'\nO maior valor sorteado foi: {max(numeros)}\nO menor valor sorteado foi : {min(numeros)}')
