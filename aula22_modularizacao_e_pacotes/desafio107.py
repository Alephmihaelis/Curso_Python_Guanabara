
'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

from moeda import *

num = int(input('Digite um valor em reais: R$'))
valor = int(input('Quanto você quer aumentar? R$'))

print('Valor total: R$', end='')
print(aumentar(num, valor))