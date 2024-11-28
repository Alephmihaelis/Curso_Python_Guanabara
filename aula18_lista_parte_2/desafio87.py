
'''
Aprimore o desafio anterior, mostrando no final:

a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha
'''

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]: '))
print('~' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()

print('~' * 40)

print(f'A soma dos números pares digitados vale {spar}')

for l in range(0, 3):
    scol += matriz[l][2]

print(f'A soma dos valores da terceira coluna vale {scol}')

for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]

print(f'O maior valor da segunda coluna é {mai}')
