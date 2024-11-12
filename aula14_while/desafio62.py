
'''
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''

print('Progressão aritmética'.upper())

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

primeiro = termo
contador = 1
total = 0
mais = 10

while mais != 0:

    total += mais

    while contador <= total:

        print('{}'.format(termo), end=' :: ')

        termo += razao

        contador += 1

    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos exibidos.'.format(total))