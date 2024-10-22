
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

ang = float(input('Ângulo: '))

# Por alguma razão, não consigo passar o `input` diretamente como radiano.

print('Seno de {}º: {:.2f}\nCosseno de {}º: {:.2f}\nTangente de {}º: {:.2f}'.format(ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))

# Inicialmente, eu havia criado a variável `rad_ang = radians(ang)`, e depois passado `rad_ang` dentro de `sin`, `con` e `tan`; mas o professor alinhou uma conversão dentro da outra. Resolvi seguir-lhe o exemplo.
