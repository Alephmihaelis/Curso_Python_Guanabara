
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27

# OBS.: Em vez de R$3.27, pus a real cotação do dólar, que hoje é R$5.69
# OBS².: Adicionei euro e iene.

alpha = float(input('Quanto dinheiro você tem? R$'))
print('\033[7;32;45mCom R${:.2f}, você pode comprar:\nUS${:.2f}\n€{:.2f}\n¥{:.2f}\033[m'.format(
    alpha,
    (alpha / 5.69),
    (alpha / 6.19),
    (alpha / 0.038)
    ))
