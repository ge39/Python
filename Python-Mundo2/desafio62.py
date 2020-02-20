'''
    desafio 62
	Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos.
	O programa encerra quando ele disser que quer mostrar.0 termo

'''

num = int(input('Digite um numero :'))
razao = int(input('Digite a Razão :'))
termo = num
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{}'.format(termo), end=" ")
        termo += razao
        contador += 1
    print('\033[31m\nPAUSA\033[m')
    mais = int(input('\033[33mQuantos termos voce quer mostrar a mais\033[m :'))
print('FIM')
