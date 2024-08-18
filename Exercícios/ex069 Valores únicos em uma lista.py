numeros  = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    s = str(input('Quer continuar: ')).strip().upper()[0]
    if s == 'N':
        break
print(f'Você digitou os valores {numeros}')
