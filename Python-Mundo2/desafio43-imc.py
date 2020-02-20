#desenvola uma lógica que leia o peso e altura de uma  pessoa, calcule seu IMC e mostre seu status
#de acordo com a tabela abaixo:

#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: peso ideal
#25 até 30: sobrepeso
#30 até 40: obesidade
#acima de 40: obesidade morbida

peso = float(input('Qual é o seu Peso (kg) :'))
altura = float(input('Sua altura (m) :'))
imc = (peso / (altura ** 2))
print('O IMC dessa pessoa é {:.2f}'.format(imc), end=" ")

if imc < 18.5:
    print('e está abaixo do peso ideal')
elif 18.5 <= imc <= 25:
    print('e está no peso ideal')
elif 25 <= imc < 30:
    print('e está com sobrepeso')
elif 30 <= imc < 40:
    print('e está obeso')
else:
    print('e está com obesidade morbida, cuidado')


