from time import sleep
from random import randint
itens = ('pedra','papel', 'tesoura')
computador = randint(0,2)
print('''
    [0 Pedra
    [1] Papel
    [2] Tesoura''')
jogador = int(input('Qual é  a sua jogada? :'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('\033[32m-=\033[m'*20)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('\033[32m-=\033[m'*20)

if computador == 0:#  PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU!!!')
        ponto = int(1)
    elif jogador == 2:
        print('VOCÊ PERDEU !!!')
    else:
        print('JOGADA INVÁLIDA 1!!!')
if computador == 1:  #PAPEL
    if jogador == 0:
        print('VOCÊ PERDEU !!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU !!!')
        ponto = 1
    else:
        print('JOGADA INVALIDA 2!!!')
if computador == 2:#  TESOURA
    if jogador == 0:
        print('VOCÊ GANHOU !!!')
        ponto = 1
    elif jogador == 1:
        print('VOCÊ PERDEU !!!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA 3!!!')

    print('Pontos', ponto)