
from math import trunc, floor

'''
Programa que lê um número real qualquer pelo teclado e mostra na tela a sua
porção inteira. Ex.: Digite um número: 6.127 -> O número 6.127 tem a parte inteira 6.
'''

print('Digite um número real.')
numReal = float(input())

'''
Há três modos de resolver este exercício.
Posso resolvê-lo ou com a função `int`, ou com o método `trunc`,
ou com o método `floor`.
'''

# Resolução com a função `int`
print('A porção inteira de {} é {}'.format(numReal, int(numReal)))

# Resolução com o método `trunc`
print('A porção inteira de {} é {}'.format(numReal, trunc(numReal)))

# Resolução com o método `floor`
print('A porção inteira de {} é {}'.format(numReal, floor(numReal)))
