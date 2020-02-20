#escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$7,00 por cada km acima do limite

from random import choice
km = (20, 40, 60, 80, 90, 100, 120, 150, 180)
speed = choice(km)
limite = 80

if speed <= 80:
    print('dentro do limite de velocidade {} km.'.format(speed))
else:
    print('Voce está a {} km.\nO limite da via é {} km.'.format(speed, limite))
    multa = float((speed - limite) * 7)
    print('voce ultrapassou o limite em {} km.'.format(speed-limite))
    print('Sua multa será de R${:.2f}'.format(multa))