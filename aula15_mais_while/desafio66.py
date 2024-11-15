
'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só parará quando o usuário digitar "999", que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o "flag").
'''

nums = soma = 0

while True:

    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    
    nums += 1
    soma += num

print('~'*30)
print(f'Você digitou {nums} números.')
print(f'A soma de todos os números vale {soma}')
print('~'*30)
