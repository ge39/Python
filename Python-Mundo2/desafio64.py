'''
    desafio 64
	crie um programa que leia varios numeros inteiros pelo teclado.
	O programa só vai parar quando o usuario digital 999, que é a condicao de parada.
	No final mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)
'''
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um numero [\033[31m999 para parar]\033[m :'))
    if num != 999:
        cont += 1  # acumula na variavel cont quantas vezes a repetição foi executado
        soma += num  # soma todos os valores digitado na variavel num
else:
        print(f'\033[34mVoce contou {cont} numeros e a soma deles são {soma}\033[m', end='')