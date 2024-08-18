from datetime import date
atual = date.today().year
a = int(input('Ano de nascimento:'))
b = atual - a
print(f'Quem nasceu em {a} tem {b} anos em {atual}.')
if b == 18:
    print(f'Você tem que se alistar esse ano')
elif b > 18:
    print(f'Você deveria ter se alistado a {b-18} atrás')
    print(f'Seu alistamento foi em {atual - (b-18)}.')
elif b < 18:
    print(f'Você precisará se alistar em {18-b} anos')
    print(f'Seu alistamento será em {(18-b) + atual}.')
    