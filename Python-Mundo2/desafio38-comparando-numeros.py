# escreva um programa que leia dois numeros inteiros e compare-os
# mostrando na tela uma mensagem

# - o primeiro valor é maior
# - o segundo valor é maior
# nao existe valor maior, os dois sao iguais

num1 = int(input('Digite o primeiro numero :'))
num2 = int(input('Digite o segundo numero :'))

if num1 > num2:
    print('\033[31mO Primeiro numero é maior que o segundo numero\033[m')
elif num1 < num2:
    print('\033[32mO Primeiro numero é menor que o segundo numero\033[m')
else:
    print('\033[34mOs dois numeros são iguais\033[m')

