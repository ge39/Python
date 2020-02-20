'''
    desafio 58
	Melhore o jogo do desafio 28, onde o computador vai 'PENSAR', em um numero entre 0 e 10.
	só que agora o jogador vai tentar adivinhar até acertar. mostrando no final quantos
	palpites foram necessarios para vencer
'''

from random import randint

computador = randint(0, 10)
acertou = False
palpites = 1
jogador = int(input('Digite o numero que pensei :'))

while not acertou:
    if jogador == computador:
        acertou = True
        print(
            'Parabéns, eu pensei no numero\033[34m {}\033[m , mas, voce precisou de\033[31m {}\033[m tentativa para acertar'.format(
                computador, palpites))
    else:
        if jogador > computador:
            print('o numero é menor, tente novamente')
        else:
            print('O numero é maior, tente novamente')
        jogador = int(input('Digite o numero que pensei :'))
        palpites += 1
