
'''
if carro.esquerda():
    True

else:
    False
'''

import emoji

tempo = int(input('Quantos anos seu carro tem: '))
if tempo <= 3:
    print(emoji.emojize('Seu carro é novo! :grinning_face_with_big_eyes:'))
else:
    print(emoji.emojize('Seu carro é velho... :sad_but_relieved_face:'))
print('Que bom que você tem um carro!')
