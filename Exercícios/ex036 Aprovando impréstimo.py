print('\033[;33m-=\033[m'*20)
a = float(input('Qual o valor da casa: R$'))
b = float(input('Qual o salário do comprador: R$'))
c = float(input('Quanto tempo de financiamento: '))
print('\033[;33m-=\033[m'*20)
parcela = (b*0.30)
financiamento = a / c
print(f'Para pagar uma casa de {a:.2f} em {c:.2f} anos a prestação será de {financiamento:.2f}')
if parcela > financiamento:
    print('Financimento \033[;32mAprovado\033[m!')

elif parcela == financiamento:
    print('Financimento \033[;32mAprovado\033[m!')

else:
    parcela < financiamento
    print('Financiamento \033[;31mNegado!\033[m')
