
'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ele pode formar um triângulo ou não.
'''

seg_um = float(input('Primeiro segmento: '))
seg_dois = float(input('Segundo segmento: '))
seg_tres = float(input('Terceiro segmento: '))

if seg_um + seg_dois > seg_tres and seg_um + seg_tres > seg_dois and seg_dois + seg_tres > seg_um:
    print('As medidas informadas podem formar um triângulo!')
else:
    print('As medidas informadas não podem formar um triângulo.')
