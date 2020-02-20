'''
    Crie um programa que tenha uma tupla unica com nomes de produtos e seus
    respectivos preços, na sequencia.
    No final, mostre uma listagem de preços, organizando os dados em forma tabular
'''
print('-'*40)
print(f'{"Listagem de Preço":^40}')
print('-'*40)
listagem = ('Caderno', 1.40,
            'Livro', 34.90,
            'Estojo', 5.00,
            'Mochila', 120.30,
            'Caneta', 10.39,
            'Lapis', 2.45,
            'Lápis de cor', 12.60)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'\033[34m{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R$ {listagem[pos]:>5}\033[m')
print('-'*40)
