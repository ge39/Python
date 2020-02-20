#  elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
#  preço normal e condição de pagamento:

# 1- a vista dinheiro/cheque: 10% de desconto
# 2- a vista no cartao: 5% de desconto
# 3- em até 2 vezes no cartao: preço normal
# 4- 3 vezes ou mais no cartao: 20% de juros

print('{#^40}\033[31mForma de pagamento\033[m')
print('\033[34m\n'
      '    1 - DINHEIRO / CHEQUE\n'
      '    2 - CARTÃO DÉBTO\n'
      '    3 - CARTÃO 2 VEZES\n'
      '    4 - CARTÃO ACIMA DE 2 VEZES\033[m')
print('=' * 100)
valor = float(input('Digite o valor da compra R$ '))
pagto = int(input('Digite a forma de pagamento :'))

if pagto == 1:
    print('Pagamento em dinheiro ou cheque')
    desconto = valor * 0.10
    total = valor - desconto
    print(
        ''' 
    Valor da compra R$ {:.2f}
    Desconto de R$ {:.2f}
    Total a pagar\033[36m R$ {:.2f}\033[m
    '''.format(valor, desconto, total))
elif pagto == 2:
    print('Pagamento no cartão de débito')
    desconto = valor * 0.05
    total = valor - desconto
    print('Valor da compra R$ {:.2f}'.format(valor))
    print('Desconto R$ {:.2f}'.format(desconto))
    print('Total a pagar\033[36m R$ {:.2f}\033[m'.format(total))
elif pagto == 3:
    print('Pagamento em 2 vezes no cartão')
    print('Valor da compra R$ {:.2f}'.format(valor), end=' - ')
    print('2 X de R$ {:.2f}'.format(valor / 2))
    print('\033[31mPagamento sem desconto\033[m')
elif pagto == 4:
    juros = (valor * 0.20) + valor
    print('Pagamento no cartao acima de 2 vezes')
    print('Valor da compra R$ {:.2f}'.format(valor))
    print('Total a pagar: \033[31mJuros de 20% - R$ {:.2f}\033[m'.format(juros))
else:
    print('\033[31mForma de pagamento usada {} - inesistente'.format(pagto))
