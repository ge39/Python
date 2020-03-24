'''
    Crie um programa que vai ler varios numeros e colocar em uma lista
    Depois disso, Crie duas listas extras que vao conter apenas os valores pares
    e os valores impares digitados, respectivamente.
    Ao final mostre o conteudo das 3 listas geradas
'''
valores = []
par = []
impar = []
while True:
    num = int(input('Digite um numero :'))
    resp = str(input('Deseja continuar[S/N] '))
    valores.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    if resp in 'nN':
        break
print(valores)
print(f'Lista de numeros pares {par}')
print(f'Lista de numeros impares {impar}')




