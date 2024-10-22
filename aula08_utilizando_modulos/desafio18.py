
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

ang = int(input('Ângulo: '))
ang_rad = radians(ang)

# Por alguma razão, não consigo passar o `input` diretamente como radiano; por essa razão me foi necessário criar a variável `ang_rad`, em que o valor recebido pelo `input` é convertido em radiano pelo método `radians`.

print('Seno de {}º: {:.2f}\nCosseno de {}º: {:.2f}\nTangente de {}º: {:.2f}'.format(ang, sin(ang_rad), ang, cos(ang_rad), ang, tan(ang_rad)))
