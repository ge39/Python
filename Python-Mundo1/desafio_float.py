# crie um programa que leia quanto dinheiro tem
# na carteira e mostre quantos dolar ele pode comprar(USS 1.00 = R$ 3,27)
money = float(input('Quanto dinheiro voce tem :?R$'))
cota = float(3.27)
dollar = float(money/cota)

print("Com R${:.2f}, voce pode comprar USS{:.2f}".format(money,dollar),"Dolar")