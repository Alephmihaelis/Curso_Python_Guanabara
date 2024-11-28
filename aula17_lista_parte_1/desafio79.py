
'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.
'''

numeros = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Esse valor já foi informado, e portanto não foi adicionado de novo!')

    response = input('Deseja continuar? [S/N] ').upper().strip()
    if response == 'N':
        break

numeros.sort()
print('~' * 30)
print(f'Você gerou a lista {numeros}')
