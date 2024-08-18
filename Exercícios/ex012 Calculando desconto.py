real = float(input('Qual o preço do produto? R$'))
desconto = real - 0.05*real 
print(f'O produto que custava R${real:.2f}, na promoção com 5% de desconto vai custar R${desconto:.2f}')
