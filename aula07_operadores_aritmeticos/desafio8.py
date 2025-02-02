
"""
Programa que lê um valor em metros e o exibe convertido em outras unidades de comprimento.
"""

print('Digite um valor.')
valor = float(input())

print('=' * 30)
print('VALOR ORIGINAL | VALOR CONVERTIDO', sep='\t')
print(f'''{valor}m equivale(m) a {valor/1000}km
{valor}m equivale(m) a {valor/100}hm
{valor}m equivale(m) a {valor/10}dam
{valor}m equivale(m) a {valor*10:.0f}dm
{valor}m equivale(m) a {valor*100:.0f}cm
{valor}m equivale(m) a {valor*1000:.0f}mm''', sep='\t')
print('=' * 30)
