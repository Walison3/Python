peso = []
for c in range(1, 6):
    a = float(input(f'Peso da {c}ª pessoa: '))
    peso.append(a)
maior = max(peso)
menor = min(peso)
print(f'O maior peso é {maior} kg.')
print(f'O menor peso é {menor} kg.')
