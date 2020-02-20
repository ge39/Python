#escreva um programa que faça o computador pensar
#entre um numero entre zero e cinco, e peca para o usuario tentar descobrir
#qual foi o numero escolhido pelo computador.
#o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep
computador = randint(0, 5)

jogador = int(input('digite um numero :'))
print('Processando....')
sleep(3)
if jogador == computador:
    print('Parabens, o numero escolhido foi {}'.format(computador))
else:
    print('voce errou, o numero escolhido foi {}'.format(computador))




