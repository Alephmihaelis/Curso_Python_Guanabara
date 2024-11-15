
total, mil, menor, cont = 0, 0, int(), 0

barato = str()

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        mil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    question = ' '
    while question not in 'SN':
        question = input('Quer continuar? [S/N] ').upper().strip()[0]
    if question == 'N':
        break

print('~'*30)   
print(f'Total da compra: R${total:.2f}')
print(f'Número de protudos que custam mais de R$1000: {mil}')
print(f'O nome do produto mais barato, {barato}, custa R${menor:.2f}.')
print('~'*30)
