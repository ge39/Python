# ansi
# escape sequence
# style; text; background

# style #0 none; #1 bold; #4 underline; #7 negative

# text 30-branco;31-vermelho;33-amarelo;34-azul; 35-magenta; 36-ciano; 37-cinza
# background 40-branco;41-vermelho;43-amarelo;44-azul; 45-magenta; 46-ciano; 47-cinza

print('\033[1;31;40mOlá Mundo\033[m')
a = 3
b = 5

print('Os valores são: \033[33m{}\033[m e \033[31m{}\033[m'.format(a, b))

print('O valor é: \033[31m {}\033[m a outro valor é \033[34m {}\033[m'.format(a, b))
print('\033[34m next\033[m -' * 20)

print('\033[0;30;45m Os valores sao: {} e {}\033[m '.format(a, b))

nome = 'Jeremias'
print('Olá muito prazer em te conhecer {} {} {}!!!'.format('\033[4;34m', nome, '\033[m'))

nome = 'Jeremias'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretobranco':'\033[7;30m'
}
print('\033[33m next\033[m -'*20)

print('Olá muito prazer em te conhecer {}{}{}!!!'.format(cores['pretobranco'], nome, cores['limpa']))


