#escreva um programa que pergunte o salaro de um funcionario e calcule o valor do seu aumento

#para salarios superiores a R4 1.250,00, calcule aumento de 10%
#para os inferiores ou iguais o aumento é de 15%

salario = float(input('informe seu salário R$:'))
salbase = 1250
if salario <= salbase:
    ajuste = 0.15
    print('Salario ajustado em: {}% - R$ {:.2f}'.format(ajuste * 100, salario * ajuste + salario))
else:
    ajuste = 0.10
    print('Salario ajustado em: {}% - R$ {:.2f}'.format(ajuste * 100, salario * ajuste + salario))