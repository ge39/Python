#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

#Se ele ainda vai se alistar ao servico militar
#se é hora de se alistar
#se ja passou da hora de se alistar

#seu programa deve mostrar tambem o tempo que falta ou que passou do prazo

from datetime import date
ano = int(input('Qual ano que voce nasceu? :'))
ano_atual = date.today().year
idade = (ano_atual -ano)
print('Voce tem {} anos  em {}'.format(idade, ano_atual))
print('\033[33mAlistamento para nascidos no ano de {}\033[m'.format(ano_atual))

if idade == 18:
        print('\033[34mVoce tem {} anos em {} e está apto ao serviço militar\033[m'.format(idade, ano_atual))
elif idade > 18:
    print('Voce tem {} anos em {} e está atrasado em {} anos '.format(idade, ano_atual, idade - 18))
else:
    print('\033[31mVoce tem {} anos em {} , e precisa esperar mais {} ano\033[m'.format(idade, ano_atual, 18 - idade))

