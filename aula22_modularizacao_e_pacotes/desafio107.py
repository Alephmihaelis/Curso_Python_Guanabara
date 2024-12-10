
'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

from moeda import *


a = '  GERENCIADOR DE MOEDAS  '
print('~' * len(a))
print(a)
print('~' * len(a))

while True:
    num = int(input('Digite um valor em reais: R$'))
    
    a_resp = input('Deseja aumentar o valor? [S/N] ').upper().strip()
    if a_resp == 'S':
        valor = int(input('Quanto você quer aumentar? R$'))
        print('Valor total: R$', end='')
        print(aumentar(num, valor))
    r = input('Deseja continuar? [S/N] ').upper().strip()
    if r == 'N':
        break