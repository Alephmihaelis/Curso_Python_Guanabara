
# InteractiveHelp
# docstrings
# Funções com argumentos opcionais
# Escopo de variáveis
# Retorno de resultados

#################################
####### Interactive Help #######
#################################

print(help)
print(input.__doc__)

#################################
########### Docstring ###########
#################################

def contador(i, f, p): ### Parâmetro real
    '''
    Faz uma contagem e mostre na tela.
    Parâmetro `i`: início da contagem
    Parâmetro `f`: fim da contagem
    Parâmetro `p`: passo da contagem
    `return`: sem retorno
    Função criada por GUSTAVO GUANABARA do canal CursoemVídeo.
    '''

    c = i
    while c <= f:
        print(f'{c}', end='...')
        c += p
    print('Terminou.')

contador(2, 10, 2) ### Parâmetro formal
help(contador)

somar(3, 2, 5)