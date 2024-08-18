from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Digite sua opção:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*20)
print(f'O computador jogou {itens[computador]}.')
print(f'O jogador jogou {itens[jogador]}.')
print('-='*20)
if computador == 0 and jogador == 1:
    print('Jogador venceu')
elif computador == 1 and jogador == 2:
    print('Jogador venceu!')
elif computador == 2 and jogador == 0:
    print('Jogador venceu')
elif computador == jogador:
    print('Empate')
else:
    print(f'Computador venceu')
