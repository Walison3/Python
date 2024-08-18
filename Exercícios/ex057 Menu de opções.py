a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''') 
    op = int(input('>>> Qual a sua opção? '))
    print('-='*20)
    if op == 1:
        print(f'A soma entre {a} e {b} é {a + b}.')
    elif op == 2:
            print(f'A multiplicação entre {a} e {b} é {a*b}.')
    elif op == 3:
            if a > b:
                print(f'O maior número foi {a}.')
            else:
                print(f'O maior número foi {b}.')
    elif op == 4:
        print('Informe os números novamente!')
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
    else:
         print('Opção invalida. Tente novamente.') 
print('Programa finalizado. Volte sempre!')
