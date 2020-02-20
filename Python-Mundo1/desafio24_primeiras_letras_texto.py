#Crie um programa que leia o nome de uma cidade,
# #diga se ela começa ou não com o nome "SANTO"

cid =str(input("digite o nome da cidade :")).strip()

print('primeiro nome :{}'.format(cid[0:5].upper()))

print(cid[0:5].upper() =='SANTO')

print('nome da cidade é :{}'.format(cid.upper()))