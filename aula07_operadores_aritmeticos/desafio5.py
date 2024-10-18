
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

alpha = int(input('Digite um número qualquer: '))

# Como o resultado será usado para uma coisa só, não o armazenarei dentro de uma variável; em vez disso, passá-lo-ei diretamente na função format.

print('O antecessor de "{}" é "{}".\nO sucessor de "{}" é "{}".'.format(alpha, (alpha - 1), alpha, (alpha + 1)))
