
'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

print('~'*50)
print('TABUADA!')
print('\033[31mSe você digitar um valor negativo, o programa será encerrado!\033[m')
print('~'*50)

while True:
    num = int(input('Você quer ver a tabuada de que valor? '))
    if num < 0:
        break
    print('~'*15)
    for x in range(1, 11):
        print(f'{num} x {x} = {num*x}')
    print('~'*15)

print('PROGRAMA ENCERRADO!')
