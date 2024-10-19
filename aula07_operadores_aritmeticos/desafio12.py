
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Valor do produto: R$'))
print('O produto de R${:.2f} custará, com desconto de 5%, R${:.2f}'.format(preco, preco-(preco*5/100)))