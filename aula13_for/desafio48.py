
# Faça um programa que calcule a soma entre todos números ímpares que são múltiplos de 3 e que se encontram entre 1 e 500.

soma = 0
contador = 0

for num in range(1, 501, 2):
    if num % 3 == 0:
        contador = contador + 1
        soma = soma + num

print('A soma de todos os valores vale {}.\nSomaram-se {} números.'.format(soma,
                                                                           contador))
