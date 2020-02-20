# if carro.esquerda():
#    bloco1
# elif carro.direita():
#    bloco2
# elif:carro.ré():
#    bloco3
# else:
#   bloco4

nome = str(input('digite seu Pais :')).upper().strip()

if nome == 'BRASIL':
    idioma = 'Portugues'
    print('Seu idioma é: {}'.format(idioma))
elif nome == 'USA' or nome == 'inglaterra':
    idioma = 'ingles'
    print('Seu idioma é o :{}'.format(idioma))
else:
    print('Seu idioma não é reconhecido')
