
'''
Crie um programa onde o usuário possa digitar 5 valores números e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

numeros = []

for num in range(5):
    numero = int(input(f'Digite um valor: '))

    if num == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= numeros[pos]:
                numeros.insert(pos, numero)
                break
            pos +=1

print('~' * 30)
print(f'Os valores digitados, em ordem, são {numeros}')
