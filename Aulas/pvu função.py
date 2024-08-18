def LE_colheita(a, b, primavera=None, verão=None, inverno=None, outono=None):
    dia = (a + b + a)  #LE coletado por dia
    estação = int(dia) #Estação equivale a 3 dias
    print('\n')
    buf = float(input('digite a porcentagem do buf: '))
    debuf = float(input('digite a porcentagem do debuf: '))
    print('\n')
    print(f'Colheita 1ª estágio: {a} LE.')
    print(f'Colheita 2ª estágio: {b} LE. \n')
    print(f'Total de {dia} LE por dia. \n')
    print(f'A cada estação: {estação*3} LE.')
    print(f'Em todo o período: {estação*12} LE \n')
    print(f'Buf: {buf}%, ou seja, {buf*(estação*3)+estação*3} de LE a mais em um dos períodos. \n') 
    print(f'Debuf: {debuf}% ou seja, {debuf*(estação*3)+estação*3} de LE a menos em um dos períodos. \n')

# Exemplo de uso com valores personalizados para estação_primavera e estação_verão

LE_colheita(40, 60, verão=-0.12, primavera=-0.08) #120147080406 - Planta de água

LE_colheita(50, 70, outono=0.08, primavera=-0.02) #140205060401 - Planta de vento

LE_colheita(40, 60, verão=0.06, inverno=-0.02) #150101050301 - Planta de fogo

LE_colheita(50, 70, outono=0.12, inverno=-0.08) #130204090603 - Planta Elétrica