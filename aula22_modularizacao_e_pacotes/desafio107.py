
'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

from moeda import *


a = '  GERENCIADOR DE MOEDAS  '
print('~' * len(a))
print(a)
print('~' * len(a))

num = float(input('Digite um valor em reais: R$'))
valor = float(input('Quanto você quer aumentar? R$'))
print('Valor total: R$', end='')
print(aumentar(num, valor))

print('=' * 40)

num = float(input('Digite um valor em reais: R$'))
valor = float(input('Quanto você quer aumentar? R$'))
print('Valor total: R$', end='')
print(diminuir(num, valor))

print('=' * 40)

num = float(input('Digite um valor em reais: R$'))
print('Valor total: R$', end='')
print(dobro(num))

print('=' * 40)

num = float(input('Digite um valor em reais: R$'))
print('Valor total: R$', end='')
print(metade(num))
