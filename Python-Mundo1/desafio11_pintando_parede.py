#faça um programa que leia a largura e a altura de uma parede em metros,
#calcule sua área e a quantidade de tinta necessária para pinta-la.
#sabendo que, cada litro de tinta, pinta uma área de 2m2

altura = float(input('Digite a Altura :'))
largura = float(input('digite a largura :'))
area = float(largura * altura)
tinta = float(area/2)

print("Dimensão da Parede : {} x {} e area de : {:.2f} M2  total de tinta {:.2f} litros".format(altura,largura,area,tinta))
