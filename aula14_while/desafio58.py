
'''
Melhore o jogo do desafio 28, onde o computador vai pensar em um número de 0 a 10;
agora o jogador tentará adivinhar até acertar. O programa deverá mostrar no final
quantos palpites foram necessários para vencer.
'''

from random import randint
from time import sleep
import emoji

palpites = 0
pc = randint(0, 10)

print('='*20)
print('JOGO DA ADIVINHAÇÃO!')
print('='*20)

print('Pensarei em um número entre 0 e 10.\nVejamos se você consegue adivinhá-lo!')
jogador = int(input('Em que número eu pensei? '))

while jogador != pc:
    palpites += 1
    print('\033[31mCalculando...\033[m')
    sleep(1)
    print('Você errou!')
    
    if jogador < pc:
        print('Mais... Tente de novo!')
    if jogador > pc:
        print('Menos... Tente de novo!')
    
    jogador = int(input('Em que número eu pensei? '))

print('-='*20)

if palpites > 1:
    print('Você acertou após {} palpites!'.format(palpites+1))
else:
    print('Você acertou com apenas 1 palpite! Parabéns!')
    print(emoji.emojize(':fireworks:' * 10))

print('-='*20)
