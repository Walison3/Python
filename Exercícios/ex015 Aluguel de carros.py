d = float(input('Por quantos dias o carro foi alugado? '))
b = float(input('Rodou quantos KM? '))
al = 60*d
km = 0.15*b
print(f'O total a pagar é de {al + km:.2f}')
