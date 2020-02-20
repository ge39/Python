#crie um programa que digite um nomero de ponto flutuante,
#esse numero deverá ser arredondado para cima e outra função arredondada para baixo
from math import ceil, floor
num = float(input('digite um numero :'))
cima = ceil(num)
baixo = floor(num)

print('numero digitado :{}\nnumero arredondado pra cima :{}\nnumero arredondado para baixo :{}'.format(num, cima, baixo))