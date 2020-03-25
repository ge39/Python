'''
    Crie um programa, onde o usuario possa adicionar 5 valores numericos e cadastre-os em uma lista
    já na posição correta de inserção, (sem usar o sort()).
    No final, mostre a lista ordenada na tela.

'''
lista = []
for c in range(0, 5):
    n = int(input("Digite um numero :"))

    if c == 0 or n > lista[-1]:
       # se for o primeiro numero digitado ou se  for maior que o numero na lista, insere no final
       lista.append(n)
       print('Adicionado ao final da lista')
    else:
       #se nao for o primeiro numero e nem o ultimo, o numero será inserido no meio do array
      pos = 0  # posiçao zero do array
      while pos < len(lista):
         #se o numero digitado for menor ou igual que o numero da lista , determine a posição a inserir na lista
        if n <= lista[pos]:
            print(lista[0])
            lista.insert(pos, n)
            print(f'Adicionado na posição {pos} da lista...')
            break
        pos += 1
print(f'Os valores digitados em ordem foram {lista}')

