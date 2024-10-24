
'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex.: Digite um número: 1834

Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1


num = input('Número entre 0 e 9999: ').strip()
print('MILHAR: {} \nCENTENA: {} \nDEZENA: {} \nUNIDADE: {}'.format(
    num[0],
    num[1],
    num[2],
    num[3]
))

# Making this code this way will generate an error if `num` does not contain all four digits.
'''

# Teacher's code:

n = int(input('Número entre 0 e 9999: '))
print('UNIDADE: {}\nDEZENA: {}\nCENTENA: {}\nMILHAR: {}'.format(
    n // 1 % 10,
    n // 10 % 10,
    n // 100 % 10,
    n // 1000 % 10
))