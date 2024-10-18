
# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

alpha = int(input('Digite um número: '))
print('Você digitou "{}".\nO dobro de "{}" é {}.\nO triplo de "{}" é {}.\nA raiz quadrada de "{}" é {:.0f}.'.format(alpha, alpha, (alpha*2), alpha, (alpha*3), alpha, (alpha**(1/2))))