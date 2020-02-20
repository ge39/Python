'''
    Crie uma tupla preenchida com os  20 primeiros colocados da tabela do campeonato brasileiro de futebol,
    na orde, de colocação . Depóis mostre os :
    a - 05 primeiros colocados
    b - os 04 ultimos colocados
    c - times em ordem alfabética
    d - em que posicção está o time da chapecoense'''

times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo','Atlético', 'Botafogo', "Atlético-PR", 'Bahia', 'São Paulo', 'Fluminense',
         'Sporte Recife', 'Chapecoense','Ec Vitória','Coritiba', 'Avaí', 'Ponte Preta','Atlético-GO')
print('=>'*15)
print(f'Lista de Time:{times}')
print('\033[31m ='*15)
print('Os primeiros 5 times do Brasileirao\033[m')
print(f'{times[0:5]}')
print('\033[33m='*30)
print('Os 4 ultimos times')
print('\033[33m=\033[m'*30)
print(f'{times[-4:]}')
print('')
print('\033[34m='*30)
print('Times em ordem Alfabética')
print('\033[34m=\033[m'*30)
print(f'{sorted(times)}')
print('\033[32m='*30)
print('Em que posicao está o time da Chapecoense')
print('\033[32m=\033[m'*30)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}º posicão do brasileirão')