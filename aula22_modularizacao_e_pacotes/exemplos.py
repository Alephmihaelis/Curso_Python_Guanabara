
"""

Modularizar é o ato de construir módulos.
O conceito de modularização surgiu no início da época de 60.
O foco principal da modularização é dividir um programa grande em pequenos módulos.
O foco secundário é melhorar a legibilidade e facilitar a manutenção do sistema.

"""

from uteis import *

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')
