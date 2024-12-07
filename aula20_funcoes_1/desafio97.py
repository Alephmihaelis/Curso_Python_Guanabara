
'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex.: escreva('Olá, mundo!')
Saída:
~~~~~~~~~~
Olá, mundo!
~~~~~~~~~~
'''

def escreva(txt, c):
    print('~' * c)
    print(txt)
    print('~' * c)


# Programa principal
texto = input('Digite um texto qualquer: ').strip()
comp = len(texto)

escreva(texto, comp)