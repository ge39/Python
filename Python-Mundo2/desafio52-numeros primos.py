'''
    Numeros primos
'''
tot = 0
num = int(input('Digite um numero :'))

for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[33m', end=' ')
        tot += 1
    else:
        print(f'\033[31m', end=' ')
    print(c, end=" ")
print(f'\033[m\nO numero {num} foi dividido {tot} Vezes')

if tot > 2:
    print(f'Portanto o numero {num} não é Primo')
else:
    print(f'O numero {num} é Primo')
