'''
    Desenvolva um programa que leia a NOME,IDADE e SEXO de 4 pessoas
    No final do programa mostre :
    A média de idade do grupo
    Qual o nome do  homem mais velho
    Quantas mulheres tem menos de 20 anos
'''
mediaidade = 4
maisnovo = maisvelho = 0
totalM = media = contador = 0
nome = ''

for p in range(1, 5):
    print('\033[33m='*40)
    print(f'Digite os dados da {p}ª pesooa')
    print('=\033[m'*40)
    pessoa = str(input(f'Digite o nome da {p}ª pessoa :')).strip().upper()
    idade = int(input('Idade :'))
    sexo = str(input('Sexo [M/F]:')[0]).strip()
    contador += 1
    media += idade / mediaidade

    if p == 1 and sexo in 'Mm':
        maisvelho = idade
        maisnovo = idade
    else:
        if idade <= maisnovo:
            maisnovo = idade
        elif idade >= maisvelho:
            maisvelho = idade
            nome = pessoa
    if sexo in 'Ff' and idade < 20:
            totalM += 1

print(f'A media das idades = {media:.2f}\nO Homem mais velho tem {maisvelho} anos e seu nome é {nome}\n{totalM} Mulheres tem menos de 20 anos')



