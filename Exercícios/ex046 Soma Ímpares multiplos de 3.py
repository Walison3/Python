soma = 0
cont = 0 
for mult in range(1, 501, 2):
    if mult % 3 == 0:
        cont = cont + 1 #Soma os elementos 
        soma = soma + mult #acumula os elementos.
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
