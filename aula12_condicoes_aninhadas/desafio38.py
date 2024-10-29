
# Escreva um programa que leia dois números inteiros e os compare, mostrando na tela uma das seguintes mensagens: O primeiro valor é maior; o segundo valor é maior; não existe valor maior: os dois são iguais.

text = {
    'bold': '\033[1m',
    'limpa': '\033[m'
}

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O primeiro valor é {}maior{} que o segundo'.format(
        text['bold'],
        text['limpa']
    ))

elif num2 > num1:
    print('O segundo valor é {}maior{} que o primeiro'.format(
        text['bold'],
        text['limpa']
    ))

else:
    print('Ambos os valores são {}iguais{}'.format(
        text['bold'],
        text['limpa']
    ))
