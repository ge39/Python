'''
    soma dos numeros pares
'''
soma = total = 0
for cont in range(1, 501):
    if cont % 2 == 0:
        soma += 1
        total += cont
print(f'A soma dos {soma} numeros pares é {total}', end='')