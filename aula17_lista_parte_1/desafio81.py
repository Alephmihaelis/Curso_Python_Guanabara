
'''
Crie um programa que leia vários números e os coloque em uma lista.
Depois, mostre:

a) Quantos números foram digitados
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = []
cont = 0

cinco = False

while True:
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    cont += 1

    if 5 in numeros:
        cinco = True

    response = input('Deseja continuar? [S/N] ').upper().strip()

    if response == 'N':
        break

print('~' * 20)
print(f'Você digitou {cont} números.')
numeros.sort(reverse=True)
print(f'A lista gerada por você, em ordem decrescente, é {numeros}')
print(f'O valor está na lista? {"Sim!" if cinco else "Não. :("}')
