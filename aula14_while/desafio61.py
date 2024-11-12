
'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma P.A.,
mostrando os 10 primeiros termos da progressão usando a estrutura `while`.
'''

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

primeiro = termo
contador = 1

while contador <= 10:
    print('{} :: '.format(termo), end='')
    termo += razao
    contador += 1
print('Fim da Progressão Aritmética')
