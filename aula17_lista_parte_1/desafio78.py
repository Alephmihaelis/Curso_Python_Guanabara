
'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posições na lista.
'''

maior = menor = None

maior_pos = menor_pos = None

numeros = []

for num in range(5):
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    
    if maior is None or valor > maior:
        maior = valor
        maior_pos = num
        
    if menor is None or valor < menor:
        menor = valor
        menor_pos = num

print(f'O maior valor foi {maior}, na posição {maior_pos}')
print(f'O menor valor foi {menor}, na posição {menor_pos}')
