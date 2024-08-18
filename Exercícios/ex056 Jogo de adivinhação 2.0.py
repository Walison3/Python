from random import randint
computador = randint(0, 10)
print('-='*20)
print('''Sou seu computador...
Acabei de pensar em um número de 0 a 10.
Será que você consegue adivinhar qual foi?''')
print('-='*20)
totalerros = 0
a = int(input('Qual seu palpite? '))
while a != computador:
    if a > computador:
        a = int(input('Menos... Qual seu palpite? '))
    elif a < computador:
        a = int(input('Mais... Qual seu palpite? '))    
    totalerros += 1
print('-='*20)    
print(f'Acertou com {totalerros + 1} tentativas. Parabéns.')
