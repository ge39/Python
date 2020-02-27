'''
    Crie um programa, onde o usuario possa adicionar 5 valores numericos e cadastre-os em uma lista
    já na posição correta de inserção, (sem usar o sort()).
    No final, mostre a lista ordenada na tela.

'''

valor = []
for c in range(1, 6):
   num = int(input(f'Digite o {c}º numero:'))
   valor.append(num)
print(f'Lista ordenada {valor}')