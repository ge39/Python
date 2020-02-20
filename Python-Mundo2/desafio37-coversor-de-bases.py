#  escreva um programa que leia um numero inteiro qualquer e peça para o usuario
#  escolher qual será a base de conversao:

# 1-para binario
# 2-para octal
# 3-para hexadecimal

num = int(input('Digite um numero :'))
print('\033[33mEscolha uma das bases para conversão\033[m:'
'''
[1] Binario
[2] Octal
[3] Hexadecimal
''')
opcao = int(input('Sua opção :'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a \033[34m{}\033[m'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a \033[34m{}\033[m'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a \033[34m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')

#  [2:] fatiamento de string, exibe o resultado a partir da posição 2 até o final