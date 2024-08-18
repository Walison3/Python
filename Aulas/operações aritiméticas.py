# adição = +

# subtração = -

# multiplicação = *

# divisão = /

# potencia = **

# divisão_inteira = //

# resto_da_divisão = %

adição = 5 + 2
subtração = 5 - 2
multiplicação = 5 * 2
divisão = 5 / 2
potencia = 5 ** 2
raiz_quadrada = 25 ** (1/2)
divisão_inteira = 5 // 2
resto_da_divisão = 5 % 2

print(f'{adição}, {subtração}, {multiplicação}, {divisão}, {potencia}, {raiz_quadrada}, {divisão_inteira}, {resto_da_divisão}')

# Ordem de precedência

'''

1 = ()
2 = **
3 = * / // %
4 = + -

'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão é {}'.format(s, m, d), end = ' ')
print('A divisão inteira é {} e a potência é {}.'.format(di,e))

print('\n')
nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))