
'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa custará R$7.00 por cada km acima do limite.
'''

import emoji
from time import sleep

speed = float(input('Velocidade do carro: '))

print('Analisando...')
sleep(2)

if speed > 80:
    print(emoji.emojize('VOCÊ FOI MULTADO! :angry_face:\nCada quilômetro a mais te custará R$7.00.\nUma vez que ultrapassaste 80km/h, sua multa custará R${:.2f}'.format(
        (speed - 80) * 7
    )))
else:
    print(emoji.emojize('Você está dentro da velocidade permitida! :smiling_face_with_open_hands:'))
print('Tenha uma boa viagem!')
