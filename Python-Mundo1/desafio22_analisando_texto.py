# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome completo om todas as letras
# o nome com todas as letras minusculas
# quantas letras ao todo tem(sem considerar os espaços)
# quantas letras tem o primeiro nome

name = str(input("Digite seu Nome :")).strip() #remove os espaços do inicio e do fim da string

print('Seu nome em maiusculo - upper() {} '.format(name.upper()))
print('Seu nome em minusculo - lower() {} '.format(name.lower()))
print("Seu nome tem  {} caracteres incluindo os  espaços".format(len(name)))
print('Seu nome tem {} caracteres excluindo os espaços'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} caracteres '.format(name.find(' ')))

separa = name.split()
print('seu primeiro nome é {} '.format(separa[0]))
print('Seu primeiro nome tem {} caracteres'.format(len(separa[0])))