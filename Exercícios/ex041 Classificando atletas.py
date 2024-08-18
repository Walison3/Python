from datetime import date
atual = date.today().year
a = int(input(f'Ano de nascimento:'))
idade = atual - a
print(f'O atleta tem {idade} anos.' )
if idade <=9:
    print(f'Classificação: MIRIM')
elif idade > 9 or 14:
    print(f'Classificação: INFANTIL')
elif idade > 14 or 19:
    print(f'Classificação: Junior')
elif idade > 19 or 25:
    print(f'Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
