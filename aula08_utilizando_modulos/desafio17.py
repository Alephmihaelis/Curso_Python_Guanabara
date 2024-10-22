
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjacente: '))

print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {:.2f}'.format(cat_op, cat_ad, hypot(cat_op, cat_ad)))

# Fiz o exercício apenas em linguagem de programação.
