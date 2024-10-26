
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

colors = {
    'amarelo': '\033[33m',
    'limpa': '\033[m',
    'vermelho': '\033[31m'
}

alpha = float(input('Digite em metros a largura da parede: '))
beta = float(input('Digite em metros a altura da parede: '))

print('{}Uma parede de{} {}{:.0f}x{:.0f}{} {}tem uma área de{} {}{:.3f}m²{}. \n{}Necessitar-se-á de{} {}{:.2f}l{} {}de tinta para ser pintada.{}'.format(
    colors['amarelo'],
    colors['limpa'],
    colors['vermelho'],
    alpha,
    beta,
    colors['limpa'],
    colors['amarelo'],
    colors['limpa'],
    colors['vermelho'],
    (alpha * beta),
    colors['limpa'],
    colors['amarelo'],
    colors['limpa'],
    colors['vermelho'],
    (alpha * beta) / 2,
    colors['limpa'],
    colors['amarelo'],
    colors['limpa']
    ))
