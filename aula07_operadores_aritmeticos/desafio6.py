
# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

alpha = int(input('Digite um número: '))
print('Você digitou "{}".\nO dobro de "{}" vale {}.\nO triplo de "{}" é {}.\nA raiz quadrada de "{}" vale {:.2f}.'.format(alpha, alpha, (alpha*2), alpha, (alpha*3), alpha, (alpha**(1/2))))

# Feito com uma variável só, porque o resultado é exibido uma só vez.