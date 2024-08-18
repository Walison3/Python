from random import randint
print('-='*20)
print('VAmOS JOGAR PAR OU ÍMPAR')
print('-='*20)
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    parimp = ' '
    while parimp not in 'PI':
        parimp = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} é computador jogou {computador}. Total de {jogador + computador}.')
    if parimp == 'P':
        if (jogador + computador) % 2 == 0:
            print('Você VENCEU!') 
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    elif parimp == 'I':
        if (jogador + computador) % 2 == 1:
            print('Você VENCEU')
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes.')