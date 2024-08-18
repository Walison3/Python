numeros = []
for c in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Voce digitou os números {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições', end=' ')
for i, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{i}', end='')
print()
print(f'O menor valor digitado foi {min(numeros)} nas posições', end=' ')
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{i}', end='')
print()

