
"""

Modularizar é o ato de construir módulos.
O conceito de modularização surgiu no início da época de 60.
O foco principal da modularização é dividir um programa grande em pequenos módulos.
O foco secundário é melhorar a legibilidade e facilitar a manutenção do sistema.

Vantagens:

1. Organização de código
2. Facilidade de manutenção
3. Ocultação de código detalhado
4. Reutilização dos módulos em outros projetos

Se os módulos ficarem muito grandes, você pode usar os PACOTES.

`Pacote` é uma pasta com vários módulos.

"""

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
#print(f'O dobro de {num} é {numeros.dobro(num)}')
#print(f'O triplo de {num} é {numeros.triplo(num)}')
