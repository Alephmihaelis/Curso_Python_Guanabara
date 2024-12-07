
'''
Faça um programa que tenha uma lista chamada números e duas funções chamada sorteia() e somaPar(). A primeira função vai sortear 5 números aleatórios e vai colocá-los dentro da lista e a segunda função vai mostrar a soma de todos os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep

numeros = list()

def sorteia(lista):
    print('Sorteando cinco valores aleatórios: ', end='')
    for c in range (0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista}, tem-se: {soma}')

sorteia(numeros)
somaPar(numeros)