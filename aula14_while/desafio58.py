
'''
Melhore o jogo do desafio 28, onde o computador vai pensar em um número de 0 a 10;
agora o jogador tentará adivinhar até acertar. O programa deverá mostrar no final
quantos palpites foram necessários para vencer.
'''

from time import sleep
from random import randint
import emoji

num_pc = randint(0, 10)

palpites = 0

print('='*20)
print('jogo da adivinhação'.upper())
print('='*20)

print('Eu, seu computador, acabei de pensar em um número entre 0 e 10.')

jogador = int(input('Em que número eu pensei? '))

while jogador != num_pc:
    palpites += 1
    print('\033[31mConferindo...\033[m')
    sleep(0.5)
    if num_pc > jogador:
        print('Mais... Tente novamente!')
    elif num_pc < jogador:
        print('Menos... Tente novamente!')
    jogador = int(input('Em que número eu pensei? '))

print('='*20)
print('Você acertou!'.upper(), emoji.emojize(':fireworks:' *3))
print('='*20)

if palpites == 1:
    print('Ao todo, você precisou de 1 palpite!')
elif palpites > 1:
    print('Ao todo, você precisou de {} palpites!'.format(palpites+1))
