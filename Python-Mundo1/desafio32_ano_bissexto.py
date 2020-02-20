# faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('que ano quer analisar ? coloque 0 para o ano atual :'))

from datetime import date

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))
