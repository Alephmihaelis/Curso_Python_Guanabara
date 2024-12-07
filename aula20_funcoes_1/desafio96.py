
'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno (lagura e comprimento) e mostre a área do terreno.
'''

def calcula_area():
    larg = float(input('Largura do terreno (m): '))
    alt = float(input('Altura do terreno (m): '))
    print(f'A área de um terreno {larg}x{alt} vale {larg * alt}m² ')

print('~' * 30)
print('Calculando área de um terreno')
print('~' * 30)
calcula_area()