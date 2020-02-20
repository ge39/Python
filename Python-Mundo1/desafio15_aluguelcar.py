#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#calcule o preço a pagar, sabendo que o carro custa R$60,00
#por dia e R$0,15 por KM rodado.

km = int(input('informe quantos km o carro percorreu :'))
diariakm = float(0.15)
dia = int(input('Informe quantos dias ficou com o carro :'))
diariacar = float(60.00)
total = float(km * diariakm + dia * diariacar)
print()
print('km percorrido: {}km valor do Km: R${}'.format(km,diariakm))
print('dias utilizados {} dias valor diaria R${:.2f}'.format(dia,diariacar))
print()
print('valor em km R${:.2f}'.format(km * diariakm))
print('valor das diarias R${:.2f}'.format(dia * diariacar))
print()
print('VALOR TOTAL DO ALUGUEL R${:.2f}'.format(total))