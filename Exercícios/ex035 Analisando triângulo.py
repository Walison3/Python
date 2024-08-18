print('-='*20)
print('\033[1;30;41mAnalisador de Triângulos\033[m')
print('-='*20)
a = int(input('Primeiro segmento:'))
b = int(input('Segundo segmento:'))
c = int(input('Terceiro segmento:'))
if a + b > c and a + c > b and b + c > a:
    print('A condição pode formar um triângulo')
else:
    print('A condição não pode formar um triângulo')
