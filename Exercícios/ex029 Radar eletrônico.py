vel = float(input('Qual a velocidade atual do carro? '))
a = (vel - 80)*7

if vel <= 80.00:
    print('Tenha um bom dia! Diriga com segurança!')
else:
    print('\033[;31mMultado, Você excedeu o limite permitido que é de 80Km/h\033[m')
    print(f'Você deve pagar uma multa de \033[4;45mR${a:.2f}\033[m')
    print('Tenha um bom dia! Diriga com segurança!')
