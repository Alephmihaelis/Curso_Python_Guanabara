
'''
Faça um programa que leia três números e mostre qual o maior e qual é o menor.
'''

from time import sleep

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

maior = num1

print('Dos três números ditos, o maior e o menor são...')
sleep(1)

if num2 > maior and num2 > num3:
    maior = num2
if num3 > maior and num3 > num2:
    maior = num3

print('O maior número é: {}'.format(maior))

menor = num2
if num1 < menor and num1 < num3:
    menor = num1
if num3 < menor and num3 < num1:
    menor = num3

print('O menor número é: {}'.format(menor))
