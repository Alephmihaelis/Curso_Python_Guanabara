
# Parte I.

'''
Funções têm por objetivo o fazer constantemente coisas que serão constantemente necessárias.
'''

def lin():
    print('—' * 30)

def mensagem(msg):
    print('—' * 30)
    print(msg)
    print('—' * 30)

mensagem('APRENDENDO FUNÇÕES!')
mensagem('Python é muito legal!')
mensagem('I heard you struck my son...')

#################################################

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B vale {s}')

soma(4, 5)