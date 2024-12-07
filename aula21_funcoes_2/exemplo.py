
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


##### Parâmetro opcional #####
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(8, 4)
somar()

########################
## Escopo de variável ##
########################

n = 2
print(n)
print(f'No programa principal, {n} vale 2')

def teste():
    x = 8
    print(f'Na função `teste`, n vale {n}')
    print(f'Na função `teste`, x vale {x}')

#### ESCOPO GLOBAL x ESCOPO LOCAL ####

def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}')

funcao()
n1 = 2
print(f'n1 global vale {n1}')

############################
#### Retorno de valores ####
############################

def somar2(a=0, b=0, c=0):
    s = a+b+c
    return s

r1 = somar2(3,2,5)
r2 = somar2(2,2)
r3 = somar2(6)
print(f'Os cálculos deram {r1}, {r2}, {r3}')



def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2}, {f3}')

def parImpar(num=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(parImpar(num))
