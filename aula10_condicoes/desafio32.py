
'''
Faça um programa que leia um ano qualquer na tela e mostre se ele é bissexto.
'''

from datetime import date
from time import sleep

print('Vamos analisar se um ano é bissexto.')
year = int(input('Digite um ano, ou coloque 0 para analisar o ano atual: '))

print('Analisando...')
sleep(1.0)

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é BISSEXTO'.format(
        year
        ))
else:
    print('O ano {} não é BISSEXTO.'.format(
        year
        ))
