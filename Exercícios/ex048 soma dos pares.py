soma = 0
for pares in range(1, 7):
    num = int(input(f'Digite o {pares} valor: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma dos números pares são {soma}')
