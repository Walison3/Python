salario = float(input('Qual é o salário do funcionário R$'))
aumento = salario
if salario > 1250.00:
    aumento = (salario*0.10) + salario
else:
    aumento = (salario*0.15) + salario
print(f'O aumento do salário de quem ganhava R${salario:.2f} passou a ser de R${aumento:.2f}')
