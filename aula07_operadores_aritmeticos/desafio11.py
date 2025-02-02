"""
Programa que lê a largura e a altura de uma parede em metros,
calcula sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2m².
"""
colors = {
    'amarelo': '\033[33m',
    'limpa': '\033[m',
    'vermelho': '\033[31m'
}

print('Digite (em metros) a largura da parede.')
larguraParede = float(input())

print('Digite (em metros) a altura da parede.')
alturaParede = float(input())

print('{}Uma parede de{} {}{:.0f}x{:.0f}{} {}tem uma área de{} {}{:.3f}m²{}. \n{}Necessitar-se-á de{} {}{:.2f}l{} {}de tinta para ser pintada.{}'.format(
    colors['amarelo'],
    colors['limpa'],
    colors['vermelho'],
    larguraParede,
    alturaParede,
    colors['limpa'],
    colors['amarelo'],
    colors['limpa'],
    colors['vermelho'],
    (larguraParede * alturaParede),
    colors['limpa'],
    colors['amarelo'],
    colors['limpa'],
    colors['vermelho'],
    (larguraParede * alturaParede) / 2,
    colors['limpa'],
    colors['amarelo'],
    colors['limpa']
    ))
