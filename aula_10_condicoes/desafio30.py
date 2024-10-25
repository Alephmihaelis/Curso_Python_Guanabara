
'''
Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é par ou ímpar.
'''

from time import sleep

num = int(input('Digite um número para saber se ele é par ou ímpar: '))

print('Analisando...')

sleep(1.3)

if num % 2 == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))
