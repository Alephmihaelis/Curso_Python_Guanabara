
'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

valores = [
    [],
    []
]
valor = 0

for v in range(7):
    valor = int(input('Digite um valor: '))

    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)


print('~' * 30)

valores[1].sort()
print(f'Os números ímpares, em ordem crescente, são: {valores[1]}')

valores[0].sort()
print(f'Os números pares, em ordem crescente, são: {valores[0]}')
