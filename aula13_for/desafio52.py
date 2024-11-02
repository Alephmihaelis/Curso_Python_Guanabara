
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número inteiro: '))

tot = 0 # Contador

for x in range(1, num+1):
    if num % x == 0:
            tot = tot + 1
            print('\033[31m', end='')
    else:
          print('\033[33m', end='')
    print(x, end=' ')

print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))

if tot == 2:
      print('Portanto, ele É primo!')

else:
      print('Portanto, ele NÃO É primo!')