# crie um algoritmo que leia um numerico e mostre
# o seu dobro, triplo e raiz quadrada.
from math import sqrt, ceil, floor

n1 = int(input('digite um numero :'))
dobro = int(n1 * 2)
triplo = int(n1 * 3)
#raiz = (n1 **(1/2))

print("Numero digitado:{}\n O dobro de: {} é {}\n O triplo de: {} é {}\n Raiz Quadrada {}".format(n1, n1, dobro, n1, triplo, sqrt(n1)))
