# crie um programa que leia um numero real qualquer
# pelo teclado e mostre na tela a sua porção inteira

from math import trunc

num = float((input('Digite um numero :')))
result = trunc(num)
print('Voce digitou:{}\nNumero inteiro:{}'.format(num, result))
