frase = 'Curso em Video Python'
print (frase[3]) 
print (frase [3:13])
print (frase[:14])
print (frase[15:])
print (frase[0:21:2])
print (frase[1::2])
print (frase[:15:2])
print (frase[::2])

print(frase.count('o')) #Quantas vezes tem a letra 'O' dentro de frase.
print(frase.upper().count('O')) #joguei as letras 'o' para Maisculo e contei quantos tinham.
print(len(frase)) #para saber o tamanho da string.
print(len(frase.strip())) #strip retira os espaçamentos das bordas.
print(frase.replace('Python', 'Android')) #troca a posição da string por outra.
print('Curso' in frase) # verifica se é verdadeiro ou falso 
print(frase.find('Curso'))
print(frase.lower().find('video'))
print(frase.split()) #['Curso', 'em', 'Video', 'Python']
dividido = frase.split() 
print(dividido[0]) #Curso
