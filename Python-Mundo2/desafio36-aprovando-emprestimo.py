#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#o programa vai perguntar o valor da casa, o salário do comprador e em qunatos anos ele vai pagar

#calcule o valor da pretação mensal
#sabendo que ela não pode exceder 30% do salário do ou então o emprestimo será negado.

valor_im = float(input('Qual o valor casa ?: R$'))
salario = float(input('Informe seu salario R$:'))
nparcelas = int(input('Quantas parcelas :'))

#calculos da prestação mensal
vparcelas = (valor_im / nparcelas)
scomprometido = (salario * 30 /100)
print('\033[34m Pesquisando Crédito\033[m - '*2)

if vparcelas <= scomprometido:
    print('Financiando em : {} parcelas\ne mensalidades de: R$ {:.2f}'.format(nparcelas, vparcelas))
    #print('\033[34mFinanciamento Aprovado\033[m - '*5)
    print('\033[34mCrédito Aprovado\033[m - ')
else:
    print('Valor da mensalidade R$ {:.2f}'.format(vparcelas))
    print('Seu sálario de R$ {:.2f} e o valor comprometido de R$ {:.2f} é inferior ao valor das parcelas'.format(salario, scomprometido))
    print('\033[31mCrédito Reprovado\033[m - ' * 5)