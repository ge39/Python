#desenvolva um programa que pergunte a distancia de uma viagem ekm.
#calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
#e R$0,45 para viagens mais longas.

distancia = int(input('Qual a distancia da viagem ? '))

if distancia <= 200:
   print('custo da viagem por km R${:.2f}'.format(distancia * 0.50))
else:
    print('custo da viajem por km R${:.2f}'.format(distancia * 0.45))

