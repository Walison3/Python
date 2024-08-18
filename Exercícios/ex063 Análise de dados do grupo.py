def lin():
    print('-'*20)

totidade = 0
totmasc = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if totidade >=18:
        totidade += 1
    if sexo == 'M':
        totmasc += 1
    lin()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{totidade} pessoas são maiores de 18 anos.')
print(f'{totmasc} são homens')
