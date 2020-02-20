'''
    Faça um programa que jogue par ou impar om o computador
    o jogo será interrompido quando o jogador perder
    mostrando o total de vitórias consecutivas
    que ele conquistou no final do jogo
'''

from random import randint
p = i = num = jogada = vitoria = derrota = 0
computador = randint(0, 6)
continuar = 'S'

while True:
    jogador = int(input('Digite um numero :')[0])
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Voce quer par [p] ou impar[i] :')).strip().upper()[0]
        print(f'Voce jogou {jogador} e o computador jogou {computador}')
        if tipo == 'P':
            if total % 2 == 0:
               vitoria += 1
               print('\033[32mVOCE VENCEU!!\033[m')
            else:
                print('VOCE PERDEU!!')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('\033[32mVOCE VENCEU!!\033[m')
            else:
                print('VOCE PERDEU!!')
    print('*' * 20)
