
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o número for ímpar, desconsidere-o.

print('='*42)
print('Leremos seis números; depois os somaremos!'.upper())
print('='*42)

soma = 0
cont = 0

for num in range(6):
    number = int(input('Número a ser somado: '))
    if number % 2 == 0:
        soma = soma + number
        cont = cont + 1

print('O resultado da soma, considerando só os numeros pares, vale {}.\nNo total, somaram-se {} números.'.format(soma, cont))