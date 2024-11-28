
'''
Crie um programa que lerá vários números e os colocará numa lista.
Depois, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

numeros = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))

    response = input('Deseja continuar? [S/N]: ').upper().strip()

    if response not in ('S', 'N'):
        print('Resposta inválida. Tente novamente.')
        continue

    numeros.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    if response == 'N':
        break

print('~' * 30)

print(f'Sua lista completa é: {numeros}')
print(f'Sua lista só com os números pares é {pares}')
print(f'Sua lista só com os números ímpares é {impares}')
