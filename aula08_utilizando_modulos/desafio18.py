
"""
Programa que lê um ângulo qualquer e
mostra na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import radians, sin, cos, tan

print('Ângulo:')
angulo = float(input())

print('Seno de {}º: {:.2f}\nCosseno de {}º: {:.2f}\nTangente de {}º: {:.2f}'.format(
angulo,
sin(radians(angulo)),
angulo,
cos(radians(angulo)),
angulo,
tan(radians(angulo))
))
