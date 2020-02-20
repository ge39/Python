'''
    desafio57
	faça um programa que leia o sexo de uma pessoa,
	mas só aceite os valores M ou F.
	caso esteja errado, peça a digitação novamente até ter um valor correto
'''

sexo = str(input('Digite seu sexo :')).strip().upper()[0]# fatiando pra pegar só a primeira letra
while sexo not in 'FfMm':   #while 'M' != sexo != 'F':
    sexo = str(input('Você errou, Digite novamente o sexo :')).upper().strip()
if sexo == 'F':
    F = str('Feminino')
    print('Informação, {} para {} está correta'.format(sexo, F))
else:
    M = str('Masculino')
    print('Informação {} para {} está correto'.format(sexo, M))

