compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    print(f'Sua compra de R${compras:.2f} vai custar R${compras - compras*0.10:.2f}')
elif opção == 2:
    print(f'Sua compra de R${compras:.2f} vai custar R${compras - compras*0.05:.2f}')
elif opção == 3:
    print(f'Sua compra de R${compras:.2f} vai custar 2 parcelas de R${compras / 2:.2f}')
elif opção == 4:
    parcelas = int(input('Em quantas parcelas? '))
    juros = (compras / parcelas)*0.20
    print(f'Sua compra de R${compras:.2f} vai custar {parcelas} parcelas de R${(compras / parcelas) + juros:.2f}')
