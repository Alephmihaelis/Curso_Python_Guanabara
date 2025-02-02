
"""
Programa que lê quanto dinheiro uma pessoa tem na carteira,
e mostra quantos dólares ela pode comprar. Considere US$1.00 = R$3.27
OBS.: Em vez de R$3.27, pus a real cotação do dólar, que hoje é R$5.69
OBS².: Adicionei euro e iene.
"""

print('Quantos reais você tem? R$')

reais = float(input())

print(f'''Com R${reais:.2f}, você pode comprar:
US${reais / 5.69:.2f}
€{reais / 6.19:.2f}
¥{reais / 0.038:.2f}''')
