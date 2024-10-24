
'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
'''

name = input('Digite seu nome: ').strip().title()
print('Olá, {}! \nVocê tem "Silva" no nome? {}'.format(
    name,
    'Silva' in name.split()
))
