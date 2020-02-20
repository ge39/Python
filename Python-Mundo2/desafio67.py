'''
    Faça um programa que mostre a tabuaada de varios numeros
    Um de cada vez, para cada valor digitado pelo usuario.
    O programa será interrompido quando numero solicitado for negativo
'''

print('Tabuada')
while True:
    n = int(input('\033[34mQuer ver a tabuada de qual valor?\033[m :'))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = \033[34m{n*c}\033[m')
    print('-'*35)
print('PROGRAMA ENCERRADO , NUMERO NEGATIVO')
