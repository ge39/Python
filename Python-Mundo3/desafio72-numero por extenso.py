'''
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de
   zero até vinte
   Seu programa deverá ler um numero pelo teclado (entre 0 e 20)
   e mostra-lo por extenso
'''
n = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
     'Doze', 'Treze', 'Quatorze','Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = 'S'
while True:
    while continuar in 'Ss':
        num = int(input('Digite um numero entre 0 e 20 :'))
        if 0 <= num <= 20:
             break
        print('Tente Novamente', end=' ')
    print(f'Voce digitou o numero {n[num]}')
    continuar = str(input('Quer continuar [S/N] :'))
    if continuar not in 'Ss':
        break
print('Sistema Finalizado')


