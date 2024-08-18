soma = 0
cont = 0
while True:
    a = int(input('Digite um número[999 para parar]: '))
    if a == 999:
        break
    soma += 1
    cont += a
print(f'A soma dos {soma} valores foi {cont}.')
