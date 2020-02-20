'''
    crie um programa que leia varios numeros inteiros pelo teclado.
    o programa só vai parar quando o usuário digitar o valor 999. que é a condição de parada
    no final, mostre quantos numeros foram digitados e qual foio a soma entre eles
    (desconsiderando o flag)
'''
num = soma = cont = 0
while True:
    num = int(input('Digite um numero [999 para parar]:'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Numeros digitados foram {cont} numeros e sua soma é {soma}')
