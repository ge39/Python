'''
    soma dos impares multiplos de 3
'''
soma = 0
for cont in range(1, 500, 2):
    if cont %3 == 0:
        soma += cont
print(soma, end=' ')