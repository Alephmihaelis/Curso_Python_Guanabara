
'''
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex.: 5! = 5x4x3x2x1 = 120


Há duas formas de calcular o fatorial de um número em Python: a primeira é com a biblioteca `math`; a outra, com o loop `while`.
Primeiro método, com `math`:

from math import factorial

num = int(input('Digite um número para saber-lhe seu fatorial: '))
print('O fatorial de {} vale {}'.format(num, factorial(num)))

Segundo método, com `while`:


n = int(input('Digite um número para saber-lhe seu fatorial: '))

contador = n
fatorial = 1

print('O fatorial de {}! é'.format(n))

while contador > 0:

    print('{}'.format(contador), end='')

    print(' x ' if contador > 1 else ' = ', end='')

    fatorial *= contador
    contador -= 1

print('{}'.format(fatorial))
'''

# Cálculo de fatorial com `for`

num = int(input('Digite um número: '))

fatorial = 1
contador = num

print('{}! equivale a '.format(num), end='')

for i in range(1, num + 1):
    print('{}'.format(contador), end='')
    fatorial *= i
    contador -= 1
    print(' x ' if contador > 0 else ' = ', end='')
print(fatorial)
