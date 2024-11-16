
'''
Crie um programa que gerará cinco números aleatórios e os colocará em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))

menor = maior = numeros[0]

print('Os números gerados foram:', end = ' ')

for n in numeros:
    print(n, end = ' ')

    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'\nO menor número é {menor}')
print(f'O maior número é {maior}')
