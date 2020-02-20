#a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e  mostre
#e mostre sua categoria, de acordo com a idade:

#  -até 9 anos mirim
#  -até 14 anos:infantil
#  -até 19 anos: junior
#  -até 20 anos: senior
#  -acima: master

from datetime import date
ano = date.today().year
nasc = int(input('Ano que nasceu :'))
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))
if idade < 9:
    print('Categoria: Mirim'.format(idade))
elif idade <= 14:
    print('Categoria: Infantil'.format(idade))
elif idade <= 19:
    print('Categoria: Junior'.format(idade))
elif idade <= 25:
    print('Categoria: Senior'.format(idade))
else:
    print('Categoria: Master'.format(idade))
