'''
    desafio 59
	crie um programa que leia 2 valores e mostre um menu na tela:
	[1] somar
	[2] multiplicar
	[3] maior
	[4] novos numeros
	[5] sair do programa

	seu programa deverá realizar a operação solicitada em cada caso.
'''
num1 = int(input('\033[32mDigite o Primeiro numero :'))
num2 = int(input('Digite o Segundo numero\033[m :'))

print('''
    [1] somar
	[2] multiplicar
	[3] maior
	[4] novos numeros
	[5] sair do programa
''')
num = 1
while num < 5:
    digite = int(input('\033[33mDigite um numero do Menu\033[m :'))
    if digite == 1:
        print(num1 + num2)
    elif digite == 2:
        print(num1 * num2)
    elif digite == 3:
        if num1 > num2:
            print('O valor \033[32m{}\033[m é maior que o valor \033[35m{}\033[m'.format(num1, num2))
        elif num1 < num2:
            print('O valor \033[32m{}\033[m é menor que o valor \033[35m{}\033[m'.format(num1, num2))
        else:
            print('Os  dois numeros \033[32m{} e {}\033[m são iguais'.format(num1, num2))
    elif digite == 4:
        num1 = int(input('\033[31mDigite o Primeiro numero\033[m :'))
        num2 = int(input('\033[31mDigite o Segundo numero\033[m :'))
    elif digite == 5:
        print('Fim')
        break
    elif digite > 5:
        print('Opção incorreta')
        num1 = int(input('\033[31mDigite o Primeiro numero\033[m :'))
        num2 = int(input('\033[31mDigite o Segundo numero\033[m :'))


        
        