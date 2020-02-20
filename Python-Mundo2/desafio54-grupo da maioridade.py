'''
    Crie uma programa qu leia o ano de nascimento de 7 pessoas.
    No final , mostre Quantas pessoas qinda nao atingiram a maioridade e quantas já são maiores.

'''

from datetime import date
atual = date.today().year
q = 1
maior = menor = 0
for q in range(1, 8):
    nasc = int(input(f'{q}-Digite o ano de nascimento :'))
    if atual - nasc < 21:
       menor += 1
    else:
        maior += 1
print(f'Total de {menor} pessoas menor de idade\nTotal de {maior} pessoas maior de 18 anos')


