#faça um programa que leia o nome completo de uma pessoa,
# monstrando em seguida o mostrando em seguida o primeiro e ultimo nome separadamente

n = str(input('digite seu nome completo :')).strip()
nome = n.split()
print('Seu primeiro nome é : {}'.format(nome[0]))
print('Seu ultimo nome é : {}'.format(nome[len(nome) -1]))