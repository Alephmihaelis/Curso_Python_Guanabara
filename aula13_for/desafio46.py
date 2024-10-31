
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

print('='*30)
print('Contagem regressiva'.upper())
print('='*30)

for second in range(10, -1, -1):
    print(second)
    sleep(1)

print(emoji.emojize(':fireworks: :fireworks: :fireworks: :fireworks:'))
