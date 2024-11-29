
'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogadas = {'1': randint(1,6),
           '2': randint(1,6),
           '3': randint(1,6),
           '4': randint(1,6)}

print('Valores tirados:')

ranking = []

for k, v in jogadas.items():
    print(f'O jogador {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('=' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: Jogador {v[0]} com {v[1]}')
    sleep(1)
print('=' * 30)
