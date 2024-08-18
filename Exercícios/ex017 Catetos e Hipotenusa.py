from math import hypot
a = float(input('Qual o comprimento do cateto adjacente:'))
b = float(input('Qual o comprimento do cateto oposto:'))
x = hypot(a, b)
print(f'A hipotenusa vai medir {x:.2f}')
