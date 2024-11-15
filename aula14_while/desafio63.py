
'''
Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
Ex.: 0, 1, 1, 2, 3, 5, 8
'''

print('='*23)
print('SEQUÊNCIA DE FIBONACCI')
print('='*23)

t1, t2 = 0, 1

num_termos = int(input('Quantos termos você quer mostrar? '))

contador = 0

while contador < num_termos:
    print(t1, ' :: ', end='')
    t1, t2 = t2, t1 + t2
    contador += 1
