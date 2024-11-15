
'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

soma = contador = media = maior = menor = 0

response = 'S'

while response == 'S':

    num = int(input('Digite um valor: '))
    contador += 1
    soma += num

    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    response = input('Deseja continuar? [S/N] ').upper().strip()

media = soma / contador

print('~'*30)
print('Você digitou {} números'.format(contador))
print('A média de todos os valores vale {}'.format(media))
print('O menor valor lido foi {}'.format(menor))
print('O maior valor lido foi {}'.format(maior))
print('~'*30)
