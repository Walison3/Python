num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma - 999}')
