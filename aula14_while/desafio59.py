
'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

opção = 0

while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')

    opção = int(input('Sua escolha: '))

    if opção == 1:
        soma = num1 + num2
        print('A soma de {} e {} vale {}'.format(num1, num2, soma))
    
    elif opção == 2:
        produto = num1 * num2
        print('O produto de {} e {} vale {}'.format(num1, num2, produto))
    
    elif opção == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        else:
            print('O maior número é {}'.format(num2))
    
    elif opção == 4:
        
        num1 = int(input('Informe o primeiro valor: '))
        
        num2 = int(input('Informe o segundo valor: '))
    
    elif opção == 5:
        print('Encerrando programa...')
        sleep(1)
        print('Programa encerrado.')
    
    else:
        print('Opção inválida!\nTente novamente.')
    print('-=-'*20)
