#  tuplas (estrutura composta)
#  listas
#  dicionarios

#   MANIPULAÇÃO DE TUPLAS
#   as tuplas são imutaveis - poderia ser uma constante
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[0:3])
print(lanche[-4])
print(lanche[0:])
print(lanche[3:])
print(lanche[:])
print('*'*30)
print(lanche)
print('*'*30)
for c in lanche:
    print(len(c))
    print(c[0:3])
print('*'*30)
for cont in range(0, len(lanche)):
    print(cont)
print('*'*30)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('*'*30)
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('*'*30)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
    #print('*'*30)
    #print(sorted(lanche))

    print('Sorted lanche')
    print(sorted(lanche))
    print('*' * 30)

    a = (2, 5, 4)       #tupla A
    b = (5, 8, 1, 2)    #tupla B
    c = a + b
    print(c)
    print('count')
    print(c.count(5))
    print('index')
    print(c.index(4))
    print('*' * 30)
    print('Tuplas como vetores')
    pessoa = ('Gustavo', 39, 'M', 99.88)
    print(pessoa)
    print('Apagando uma tupla inteira')
    del(pessoa)
    print(pessoa)

