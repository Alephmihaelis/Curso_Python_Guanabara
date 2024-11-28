
'''
Crie um programa onde o usuário possa digitar 5 valores números e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

numeros = []

for p, num in enumerate(range(5)):
    numero = int(input(f'Digite um valor na posição {p+1}: '))

    if len(numeros) == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        for i in range(len(numeros)):
            if numero <= numeros[i]:
                numeros.insert(i, numero)
                break

print(numeros)
