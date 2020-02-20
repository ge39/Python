# faça um programa que leia uma ferase pelo teclado e mostre quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez e em que posição ela aparece a ultima vez

frase = str(input("digite uma frase :")).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A') + 1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A') + 1))