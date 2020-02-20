#crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

num = int(input('digite um numero :'))
resultado = num % 2
# % = resto da divsao
print('o número {} é par'.format(num) if resultado == 0 else 'o numero {} é impar '.format(num))