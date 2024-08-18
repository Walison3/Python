'''from math import factorial
a = int(input('Digite um número para verificar o fatorial: '))
f = factorial(a)
print(f'O fatorial de {a} é {f}.')'''


a = int(input('Digite um número para verificar o fatorial: '))
f = a
fatorial = 1
while f > 0:
    print(f'{f}', end=' ')
    print('x' if f > 1 else '=', end=' ')
    fatorial *= f
    f -= 1
print(f'{fatorial}')
