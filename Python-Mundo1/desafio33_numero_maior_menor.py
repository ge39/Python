#faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor


a = int(input('digite um numero :'))
b = int(input('digite segundo numero :'))
c = int(input('digite o terceiro numero :'))

#verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('')
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado é :{}'.format(menor))
print('o maior valor digitado é :{}'.format(maior))