#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo retangulo, calcule e  mostre o comprimento da hipotenusa

from math import hypot
co = float(input('digite o cateto oposto :'))
ca = float(input('digite o cateto adjacente :'))
#h1 = (co ** 2 + ca ** 2)**(1/2) metodo convencional
h1 = hypot(co, ca)

print("valor cateto oposto :{}\nvalor cateto adjacente :{}\ncomprimento da hipotenusa :{:.2f}".format(co, ca, h1))