nome = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while nome not in 'MmFf':
    nome = str(input('Dados invalidos. Por favor informe seu sexo: [M/F] ')).upper().strip()[0]
print(f'Dados registrados com sucesso.')