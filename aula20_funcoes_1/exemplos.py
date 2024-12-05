
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
# soma(3, 9, 5) # Dá erro, porque a função só recebe dois parâmetros.

### Empacotar parâmetros ###
def contador( * num):
    tam = len(num)
    print(f'Recebi os valores {num}; ao todo, são {tam} números.')
    print('Fim')
contador(5, 7, 3, 1, 4)
contador(8, 0)
contador(8, 4, 7)
############################

valores = [7, 2, 5, 0, 4]

def dobra_valores(vls):
    pos = 0
    while pos < len(vls):
        vls[pos] *= 2
        pos +=1

dobra_valores(valores)
print(valores)