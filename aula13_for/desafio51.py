
# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
enesimo = termo + (10-1) * razao

for num in range(termo, enesimo + razao, razao):
    print(num)
