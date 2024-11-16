
'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos = (input('Produto: '),
            float(input('Preço: R$')),

            input('Produto: '),
            float(input('Preço: R$')),

            input('Produto: '),
            float(input('Preço: R$')),

            input('Produto: '),
            float(input('Preço: R$')),

            input('Produto: '),
            float(input('Preço: R$')),

            input('Produto: '),
            float(input('Preço: R$'))
                  )

for i in range (0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]:>7.2f}')
