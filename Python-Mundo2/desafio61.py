'''
    desafio 61
	Refaça  desafio 51, lendo o primeiro termo e a razão de uma PA.
	mostrando os 10 progressão usando a estrutura while
'''
num1 = 0
num2 = 0
contador = 0


num1 = int(input('Digite o Primeiro termo :'))
razao= int(input('Digite a Razão da PA :'))
termo = num1
contador = 1
continua: str = 'S'

while continua in 'Ss':
    while contador <= 10:
        print('{} '.format(termo), end='- ')
        contador += 1
        termo += razao
        print('PAUSA......')
    continua = str(input('Deseja informar ou termo ?:')).strip().upper()