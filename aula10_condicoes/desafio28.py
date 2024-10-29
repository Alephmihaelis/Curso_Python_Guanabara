
'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para que o usuário tente descobrir  o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import emoji
from random import randint # Importei somente a função `randint`, em vez de toda a biblioteca `random`. Isto economiza memória.
from time import sleep

print('Pensarei em um número entre 0 e 5. Tente adivinhá-lo!')
user_num = int(input('Número: '))
pc_num = randint(0, 5)

print('Processando...')
sleep(2)

if user_num == pc_num:
    print(emoji.emojize('PARABÉNS! Você acertou! :grinning_face_with_smiling_eyes:'))
else:
    print(emoji.emojize('Você errou! :sad_but_relieved_face:'))
