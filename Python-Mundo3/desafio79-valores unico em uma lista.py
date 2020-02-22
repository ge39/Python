'''
    crie um programa, onde o usuario possa digitar varios valores numericos
    e cadastre-os em uma lista. Caso o numero já exista lá dentro.
    Ele não será adicionado.
    No final, serão exibidos todos os valores unicos digitados em ordem crescente
'''
valor = []
dupl = []
resp = 'S'

while True:
    num = int(input('Digite um numero :'))
    resp = str(input('Quer continuar: [S/N]')).strip().upper()

    if num not in valor:
        valor.append(num)
    else:
        dupl.append(num)
        print(f'Valor\033[31m {num}\033[m já foi inserido')
    if resp in 'Ss':
        continue
    else:
        break
valor.sort()
print(f'\033[33mValores inseridos na lista foram\033[m -> {valor}')
print(f'Valores Duplicados\033[31m {dupl}\033[m ')




