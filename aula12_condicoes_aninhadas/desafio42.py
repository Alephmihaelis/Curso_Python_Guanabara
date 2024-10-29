
# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 1. EQUILÁTERO: todos os lados iguais; 2. ISÓSCELES: dois lados iguais; 3. ESCALENO: todos os lados diferentes.

colors = {
    'bold': '\033[1m',
    'limpa': '\033[m'
}

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('Os segmentos informados {}podem{} formar um triângulo.'.format(
        colors['bold'],
        colors['limpa']
    ))

    if seg1 == seg2 == seg3:
        print('O triângulo que será formado é {}EQUILÁTERO{}.'.format(
            colors['bold'],
            colors['limpa']
        ))
    
    elif seg1 == seg2 and seg1 != seg3 or seg2 == seg3 and seg2 != seg1 or seg3 == seg1 and seg3 != seg2:
        print('O triângulo que será formado é {}ISÓSCELES{}.'.format(
            colors['bold'],
            colors['limpa']
        ))
    else:
        print('O triângulo que será formado é {}ESCALENO{}.'.format(
            colors['bold'],
            colors['limpa']
        ))

else:
    print('Os segmentos informados {}não podem{} formar um triângulo.'.format(
        colors['bold'],
        colors['limpa']
    ))