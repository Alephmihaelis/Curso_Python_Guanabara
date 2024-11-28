
'''
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves
'''

temp = []
princ = []
maior = menor = None

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    
    princ.append(temp[:])
    temp.clear()

    response = input('Continuar? [S/N] ').upper().strip()

    if response == 'N':
        break

print('~' * 40)

print(f'Número de pessoas cadastradas: {len(princ)}')
print(f'O maior peso foi de {maior}kg. Peso de: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=', ')

print(f'\nO menor peso foi de {menor}kg. Peso de: ', end='')
for p in princ:
        if p[1] == menor:
            print(f'[{p[0]}]', end=', ')