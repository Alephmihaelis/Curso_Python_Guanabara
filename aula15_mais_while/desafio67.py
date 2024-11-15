
'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    num = int(input('Você quer ver a tabuada de que valor? '))
    print('~'*10)
    for x in range(1, 10):
        print(f'{num} x {x} = {num*x}')
    print('~'*10)
    response = int(input('Deseja continuar?\nSe sim, digite outro número.\nSe não, digite um número negativo. '))
    if response < 0:
        break

print('Programa encerrado.')