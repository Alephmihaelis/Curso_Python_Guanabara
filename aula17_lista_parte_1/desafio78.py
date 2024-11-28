
'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o `maior` e o `menor` valor digitados e suas respectivas posições na lista.
'''

listanum = []
maior = 0
menor = 0

for p in range(5):
    listanum.append(int(input(f'Digite um valor para a posição {p}: ')))
    if p == 0:
        maior = menor = listanum[p]
    else:
        if listanum[p] > maior:
            maior = listanum[p]
        if listanum[p] < menor:
            menor = listanum[p]

print('~' * 45)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')

print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')