'''
    desafio 65
	Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução mostre :
	a media entre todos valores
	qual foi o maior e o menor valores lidos.

	o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores
'''

continuar = 'S'
soma = quant = cont = n = media = maior = menor = 0

while continuar == 'S':
    num = int(input('Digite um numero : '))
    cont += 1
    soma += num
    media = soma / cont
    if quant == 1:
        maior = menor = num
    else:
        if num < maior:
            menor = num
        if num > maior:
            maior = num
    continuar = str(input('Deseja continuar [S/sim] [N/não] :')).upper().strip()[0]
else:
    print('\033[31mTotal de numeros {}\033[m \n\033[32mSoma dos valores {:.2f}\033[m \033[34m \ne a sua média {:.2f}\033[m\033[35m '
          '\nO maior valor foi {} e o menor valor foi {}\033[m'.format(cont, soma, media, maior, menor))
