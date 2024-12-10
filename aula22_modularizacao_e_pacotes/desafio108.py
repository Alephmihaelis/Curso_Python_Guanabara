
'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''

from moeda import moedas

num = float(input('Digite um valor em reais: '))
print(f'Você digitou {moedas(num)}')
