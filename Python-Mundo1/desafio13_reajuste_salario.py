#faça um algoritmo que leia o salario de um funcionario
#mostre seu novo salário com 15% de aumento

salario = float(input('Informe seu Salário :'))
aumento = float(input('Informe o aumento'))

print("Novo salario com aumento {}:".format(aumento * salario/100 + salario))