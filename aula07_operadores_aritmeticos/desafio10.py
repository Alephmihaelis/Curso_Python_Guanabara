
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27

# OBS.: Em vez de R$3.27, pus a real cotação do dólar, que hoje é R$5.69

alpha = float(input('Quanto dinheiro você tem? R$'))
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(alpha, (alpha / 5.69)))
