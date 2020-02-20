'''
    progressão aritmetica
'''
print('='*30)
print('TERMOS DE UMA PA' )
print('='*30)
continuar = 'S'
while True:
    if continuar in 'Ss':
        primeiro = int(input('Primeiro termo :'))
        progressao = int(input('Progressao :'))
        razao = int(input('Razao :'))
        decimo = primeiro + (progressao) * razao

        for pa in range(primeiro, decimo, razao):
          print(f'{pa}', end=' -> ')
        continuar = str(input('\nDeseja continuar[S/N] :'))
    else:
      break
print('Fim da PA')