galera = list()
dado = list()
maior = menor = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    galera.append(dado[:])
    if dado[1] >=85:
        maior.append(dado[1])
    elif dado[1] <= 65:
        menor.append(dado[1])
    dado.clear()
    continuar = str(input('Quer continuar: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Ao todo você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {max(maior)}.', end=' ')
for p in galera:
    if p[1] >=85:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {min(menor)}.', end=' ')
for p in galera:
    if p[1] <=65:
        print(f'{p[0]}', end=' ')
print()
