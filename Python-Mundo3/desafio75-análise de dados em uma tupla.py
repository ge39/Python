'''
    Desenvolva um programa que leia quatro valores pelo teclado
    e guarde-os em uma tupla.
    No final, mostre:
    A - Quantas vezes apareceu o valor 9
    B - Em que posição foi digitado o primeiro valor 3
    C - Quais foram os numeros pares
'''

num = (int(input('Digite um numero :')),
       int(input('Digite outro numero :')),
       int(input('Digite mais um numero :')),
       int(input('Digite o ultimo numero :')),)
print('='*40)
print(f'Voce digitou o numeros {num}')
print(f'O Valor 9 apareceu {num.count(9)} vezes')

if 3 not in num:
    print('O valor 3 nao apareceu em nenhuma posição !!')
else:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}')
print('Os valores pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(f' {n}', end='')





