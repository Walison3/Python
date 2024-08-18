nome = str(input('Digite o seu nome: ')).strip() #<--> retira a quantidade de espaços.
frase = nome.split()
print('Analisando o seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome completo tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu 1°nome tem ao todo {nome.find(' ')} letras')
print(f'Seu 1°nome tem ao todo {len(frase[0])} letras')
