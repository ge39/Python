'''
    faça um programa que leia o peso de cinco pessoas.
     No final, mostre qual foi o maior e o menor peso lido
'''
peso = maiorpeso = menorpeso = 0
for p in range(1, 6):
    peso = float(input(f'{p}-Qual o peso da {p}ª pessoa:'))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso <= menorpeso:
            menorpeso =peso
        elif peso >= maiorpeso:
            maiorpeso =peso
print(f'\033[32mO Maior peso é {maiorpeso}\nO menor peso é {menorpeso}')

