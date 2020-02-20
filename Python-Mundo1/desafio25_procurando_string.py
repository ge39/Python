#crie um programa que leia o nome de uma pessoa
#e diga se ela tem "SILVA" no nome

nome = str(input("digite seu nome completo :")).strip()
print("Seu nome tem silva ? {}".format('SILVA' in nome.upper()))#RETONA VALOR BOOLEANO
print("nome completo :{}".format(nome.upper()))
