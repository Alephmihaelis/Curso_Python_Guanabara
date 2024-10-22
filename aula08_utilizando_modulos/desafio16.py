
from math import trunc, floor

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127 :: O número 6.127 tem a parte inteira 6.

num_real = float(input('Digite um número real: '))

# Há três modos de resolver este exercício. Posso resolvê-lo ou com a função `int`, ou com o método `trunc`, ou com o método `floor`.

# Resolução com a função `int`
print('A porção inteira de {} é {}'.format(num_real, int(num_real)))

# Resolução com o método `trunc`
print('A porção inteira de {} é {}'.format(num_real, trunc(num_real)))

# Resolução com o método `floor`
print('A porção inteira de {} é {}'.format(num_real, floor(num_real)))
