
'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno (lagura e comprimento) e mostre a área do terreno.
'''

def calcula_area(larg, comp):
    print(f'A área de um terreno {larg}x{comp} vale {l * c}m² ')


print('~' * 30)
print('Calculando área de um terreno')
print('~' * 30)

l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))

calcula_area(l, c)