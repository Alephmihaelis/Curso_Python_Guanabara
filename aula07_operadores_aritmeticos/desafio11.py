
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

alpha = float(input('Digite em metros a largura da parede: '))
beta = float(input('Digite em metros a altura da parede: '))

print('Uma parede de {:.2f}x{:.2f} tem uma área de {:.3f}m². \nNecessitar-se-á de {:.2f}l de tinta para ser pintada.'.format(alpha, beta, (alpha * beta), (alpha * beta) / 2 ))
