from random import randint
from time import sleep

print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-'*20)

jogador = int(input('Digite um número: '))
computador= randint(0,5) #faz o computador pensar em um número no intervalo informado.
print('PROCESSANDO...')
sleep(3)

if computador == jogador:
    print('Você acertou, droga!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no número {jogador}!')
    