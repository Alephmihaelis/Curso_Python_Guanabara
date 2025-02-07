
"""
Programa que lê o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo, calcula e mostra o comprimento da hipotenusa.
"""

from math import hypot

print('Comprimento do cateto oposto:')
cat_op = float(input())

print('Comprimento do cateto adjacente:')
cat_ad = float(input())

print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {:.2f}'.format(
cat_op, cat_ad, hypot(cat_op, cat_ad)))
