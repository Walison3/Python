from datetime import datetime
atual= datetime.now().year
totmaior = 0
totmenor = 0
for idade in range(1, 8):
    data = int(input(f'Em que ano a {idade}ª pessoa nasceu? '))
    n = atual - data
    if n >=18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print(f'Ao todo tivermos {totmaior} pessoas maiores de idade.')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade.')
