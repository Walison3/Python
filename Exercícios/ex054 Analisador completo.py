nomes = []
idades = []
sexos = []
for c in range(1, 5):
    print(f'-----{c}ª PESSOA-----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).upper()
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
media = idade / 4
print(f'A média da idade do grupo é de {media} anos.')
