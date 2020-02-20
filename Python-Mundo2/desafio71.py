'''
    Crie um programa que simule o funcionamento de um caixa eletronico.
    No inicio, pergunte ao cliente qual o valor a ser sacado (numero inteiro)
    e o programa irá informar quantas cedulas de cada valor serão entrgues
    OBS: considere que o caixa possui cedulas R$ 100,00, R$ 50,00, R$ 20,00,R$ 5,00, R$ 10,00, R$ 5,00 e R$1,00
'''
print('='*30)
print('{:^30}'.format('Banco CEV'))
print('='*30)

saque = int(input('Quanto quer sacar ? R$ '))
cedula = 100
totcedula = 0
total = saque

while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'total de {totcedula} cedulas no valor de {cedula}')
        if cedula == 100:
             cedula = 50
        elif cedula == 50:
             cedula = 20
        elif cedula == 20:
             cedula = 10
        elif cedula == 10:
             cedula = 5
        elif cedula == 5:
             cedula = 2
        elif cedula == 2:
             cedula = 1
        totcedula = 0
        if total == 0:
            break
print('{:^30}'.format('\033[32mO BANCO CEV AGRADECE !!\033[m'))



