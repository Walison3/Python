a = int(input('Digite um número: '))
tot = 0
for c in range(1, a+1):
    if a % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {a} foi divisível {tot} vezes.')
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')
    