#  crie um programa que leia duas notas de um aluno e calcule sua média,
#  mostrando uma mensagem no final, e acordo com a média atingida

#  -media abaixo de 5.0:
#  reprovado
#  média entre 5.0 e 6.9:
#  recuperação
#  média 7.0 ou superior
#  aprovado

n1 = float(input('Primeira nota :'))
n2 = float(input('Segunda nota :'))
media = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('Sua média é\033[31m {}\033[m, \033[31mVocê foi reprovado\033[m'.format(media))
elif 7 > media >= 5:
    print('Sua média é \033[32m{}\033[m , Voce está de \033[32mrecuperação\033[m'.format(media))
else:
    print('\033[32mAprovado - \033[m' * 5, sep='-', end='')
    print('\033[32mAprovado\033[m')
    print('Sua média é {}, Voce está aprovado'.format(media))
