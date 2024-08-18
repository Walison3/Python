vel = float(input('Qual a distância da sua viagem: '))
print(f'Você está prestes a começar uma viagem de {vel}Km')
if vel >200.00:
    preço = vel*0.45
else:
    preço = vel*0.50
print(f'O preço da sua passagem sera de R${preço}')
