
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

alpha = int(input('Digite um número para ver-lhe a tabuada: '))

print('-'*25)

print('{} x 1 = \033[31m{}\033[m\n{} x 2 = \033[31m{}\033[m\n{} x 3 = \033[31m{}\033[m\n{} x 4 = \033[31m{}\033[m\n{} x 5 = \033[31m{}\033[m\n{} x 6 = \033[31m{}\033[m\n{} x 7 = \033[31m{}\033[m\n{} x 8 = \033[31m{}\033[m\n{} x 9 = \033[31m{}\033[m\n{} x 10 = \033[31m{}\033[m'.format(
    alpha,
    (alpha*1),
    alpha,
    (alpha*2),
    alpha,
    (alpha*3),
    alpha,
    (alpha*4),
    alpha,
    (alpha*5),
    alpha,
    (alpha*6),
    alpha,
    (alpha*7),
    alpha,
    (alpha*8),
    alpha,
    (alpha*9),
    alpha,
    (alpha*10)
    ))

print('-'*25)
