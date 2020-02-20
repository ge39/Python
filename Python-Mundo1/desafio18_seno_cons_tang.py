#faça um programa que leia um angulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians

ang = float(input('digite angulo :'))
se = sin(radians(ang))
co = cos(radians(ang))
tang = tan(radians(ang))

print('Angulo :{: .2f}\nSeno :{: .2f}\nCosseno :{:.2f} \ntangente :{: .2f}'.format(ang, se, co, tang))