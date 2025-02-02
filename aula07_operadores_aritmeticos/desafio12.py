
"""
Algoritmo que lê o preço de um produto
e mostra seu novo preço, com 5% de desconto.
"""

colors = {
    'bold': '\033[1m',
    'yellow_bg': '\033[43m',
    'limpa': '\033[m'
}

print('Preço do produto: R$')
preco = float(input())

print('{}{}O produto de R${:.2f} custará, com desconto de 5%, R${:.2f}{}'.format(
    colors['bold'],
    colors['yellow_bg'],
    preco, preco-(preco*5/100),
    colors['limpa']
    ))
