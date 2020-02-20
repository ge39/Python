'''
    Crie um programa que tenha uma tupla com varias palavras
    (não usar acentos).
    Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais
'''

palavras = ('java script', 'Python', 'Php', 'Java', 'Ruby', 'Html', 'Mysql', 'django', 'Git', 'Wordpress')

    # percorre a lista de palavras e armazena na variavel "lista"
for lista in palavras :
    print(f'\nNa palavra {lista.upper()} tem ', end=' ')

    #percorre os dados da variavel lista e armazena em "vogal"
    for vogal in lista:
     #identifica e separa os valores que estão armazenados na variavel letra
     if vogal in 'aeiou':
        print(f'\033[32m{vogal.upper()}\033[m', end=' ')
