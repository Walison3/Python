a = int(input('Qual o primeiro valor: '))
b = int(input('Qual o segundo valor: '))
c = int(input('Qual o terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'O menor valor digitado foi {menor}')