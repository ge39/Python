'''
    crie um programa que leia o nome e o preço de varios produtos
    O programa  deverá perguntar se o usuario vai continuar, e no final mostre

    A - Qual é o total gasto na compra
    B - Quantos produtos custam mais de R$ 100,00
    C - Qual o nome do produto mais barato
'''

totcompra = prod100 = menorpreco = maiorpreco = cont = 0

print('*'*60)
print('Mega Liquidação')
print('*' * 60)

while True:
    produto = str(input('Produto :')).strip().upper()
    preco = float(input('Qual o Preço R$:'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [SN]?:')).strip().upper()
        totcompra += preco
        cont += 1
        if preco > 100:
            prod100 += 1
        if cont == 1:  #se for o primeiro item do looping
            menorpreco = maiorpreco = preco

        else:
            if preco < menorpreco:
                menorpreco = preco
            if preco >= maiorpreco:
                maiorpreco = preco
    if continuar == 'N':
        break
print('\033[34m********** Dados da compra **********\033[m')
print(f'Total da compra: R$ {totcompra:.2f}')
print(f'Compra com {prod100} produtos acima de 100 reais')
print(f'O produto mais barato tem o valor de \033[34mR$ {menorpreco:.2f}\033[m')
print(f'O produto mais caro  tem o valor de \033[31mR$ {maiorpreco:.2f}\033[m')
print('{:-^40}'.format('FIM DO PROGRAMA'))