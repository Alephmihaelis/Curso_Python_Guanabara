
"""
Programa que lê um número inteiro qualquer e mostra na tela sua tabuada.
"""

print('Digite um número para ver-lhe sua tabuada.')

num = int(input())

print('=' * 25)
print(f'TABUADA DE {num}')

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}', sep='\t')

print('=' * 25)
