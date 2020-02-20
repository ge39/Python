#faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço com 5 % de desconto

preco = float(input('digite o valor? :R$'))
desconto = float(input('digite o valor do desconto :'))
novo = float(preco - (desconto * preco/100))
print('Preco Antigo R$ {:.2f} desconto {:.2f}% e o novo valor com desconto é R$ {:.2f}'.format(preco, desconto, novo))