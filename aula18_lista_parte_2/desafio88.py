
'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

lista = []
jogos = []

print('~' * 30)
print('PALPITES PARA A MEGA SENA')
print('~' * 30)

quant_jogos = int(input('Quantos jogos você quer fazer? '))

tot_jogos = 1

while tot_jogos <= quant_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot_jogos += 1

print('-=' * 3, f'Sorteando {tot_jogos} jogos ', '-=' * 3)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
