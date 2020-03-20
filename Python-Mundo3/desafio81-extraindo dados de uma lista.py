'''
    Crie um programa que leia varios numeros e coloque um uma lista
    depois disso mostre:

    A - Quantos numeros foram digitados
    B - A lista de valores ordenados de forma decrescente
    C - Se o valor 5 foi digitado e está ou não na lista
'''

lista = []

resp = "N"
while True:
    lista.append(int(input("Digite um Numero :")))
    resp = str(input("Deseja continuar [S/N]:"))
    if resp in 'Nn':
        break
#Quantos numeros foram digitados
print(f'Voce digitou {len(lista)} elementos')
#A lista de valores ordenados de forma decrescente
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente sao {lista}')

#Se o valor 5 foi digitado e se está ou não na lista
if 5 in lista:
    print('O numero cinco faz parte da lista')
else:
    print('O numero 5 não faz parte da lista')

