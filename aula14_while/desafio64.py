
'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só parará quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

soma = contador = num = 0

while num != 999:

    num = int(input('Digite um número: [999 para parar]: '))
    contador += 1
    soma += num

if num == 999:
    contador -= 1
    soma -= 999

print('~'*30)
print('Você digitou {} números'.format(contador))
print('A soma de todos os números digitados vale {}.'.format(soma))
print('~'*30)
