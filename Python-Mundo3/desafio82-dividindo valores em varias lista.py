'''
    Crie um programa que vai ler varios numeros e colocar em uma lista
    Depois disso, Crie duas listas extras que vao conter apenas os valores pares
    e os valores impares digitados, respectivamente.
    Ao final mostre o conteudo das 3 listas geradas
'''
valores =[]
while True:
    valores.append (int(input('Digite um numero :')))
    resp = str(input('Deseja continuar[S/N] '))
    if resp in 'nN':
        break
print(valores)

