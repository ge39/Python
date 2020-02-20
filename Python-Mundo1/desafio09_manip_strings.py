# manipulação de strings
# técnica de fatiamento com python
frase = 'Curso em video Python'
print(frase[0:21])# do inicio até o caracter n
print(frase[:6])# do inicio até a posicao 6, index da string
print(frase[15:])# do index 15 até o final da string
print(frase[9:21:2])# do index 9 ao 21, pulando de dois em 2
print(frase[9::3])#do index 9 até o index 21, pulando de 3 em 3 caracteres
print(frase[::2])
#Análise

#len
print(len(frase))# mostra o comprimento da string

#count
print(frase.count('o')) # conta quantas vezes a letra aparece na string

#count com fatiamentp
print(frase.count('o', 0, 13),'ocorrencias') # vai contar quantas vezes a string 'o' vai aparecer na posicao 0 (index) até a posicao 13 (index)

#find
print('Palavra video inicia na posiçao :',frase.find('video'))#informa a posicao do index que a palavra ou letras iniciam

print(frase.find('Android'))#retorno -1, indica que a string na foi encontrada

# operador in
print('Curso' in frase)#retorna um valor booleano

#Transformação

#replace
print(frase.replace('Python','Androide')) #substitui na exibição  a palavra Python por Androide

#metodo upper()
print(frase.upper())#transforma a string em maiuscula

#metodo lower()
print(frase.lower())#transfome a string em minusculas

#capitalize()
print(frase.capitalize())# somente a inicial fica maiuscula

#title()
print(frase.title())#coloca todas as iniciais em maiusculas

#strip()
frase="  Aprenda Python  "
print(frase.strip())#remove os espaços do inicio e fim da frase
#rstrip()
print(frase.rstrip())#remove os espaços da direita

#lstrip()
print(frase.lstrip())#remove os espaços da esquerda

print('divisao de string')
frase ='Curso em video Python'

#split
print('funcao split :',frase.split(' '))

#juncao
print('funcao join :')
print('-'.join(frase))
