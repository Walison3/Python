tempo = int(input('Quanto anos tem seu carro? '))

if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

print('carro novo' if tempo <=3 else 'Carro velho') #condição simplificada.
