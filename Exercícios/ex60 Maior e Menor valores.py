resposta = 'S'
soma = 0
cont = 0
maior = 0
menor = float('inf')
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num #acumulado
    cont = cont + 1 #quantidade de vezes
    if num > maior:
        maior = num
    elif num < menor:  # Verifica se o número é menor que o menor atual
        menor = num
    resposta = str(input('Quer continuar? ')).upper().strip()[0]
print(f'Á média foi {soma / cont:.2f} e o maior número digitado foi {maior} e menor valor digitado foi {menor:.0f}.')
