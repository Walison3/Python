from random import randint
sorteio = ()
print('Os números sorteados foram:', end=' ')
for num in range(5):
    c= randint(0, 10)
    sorteio += (c,)
    print(f'{c}', end=' ')

print(f'\nO maior número foi {max(sorteio)}.')
print(f'O menor número foi {min(sorteio)}.')
