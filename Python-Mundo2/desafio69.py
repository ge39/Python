'''
    CRIE UM PROGRAMA que leia a idade e sexo de várias pessoas
    a cada pessoa cadastrada, o programa deverá perguntar seo usuario quer ou nao continuar
    no final mostre.
    A - quantas pessoas com mais de 18 anos
    B - quantos homens foram cadastrados
    C - quantas mulheres tem menos de 20 anos
'''
tot18 = totH = totM20 = 0
while True:
    print('Cadastro de Pessoas')
    print('\033[34m*\033[m' * 60)
    idade = int(input('idade :'))
    sexo = ' '      #limpa a variavel

    while sexo not in 'FM':     #enquanto o valor  digitado  não for o correto [FM],  a repetição não para
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '  #limpa o  campo resposta
    while resp not in 'SN':  # se a resposta digitada for diferente de [SN], continue perguntando
        resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
        print('\033[34m*\033[m'*60)
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
