
'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(n, show=False):
    '''
    Função que calcula o fatorial de um número.
    n: número a ser calculado;
    show (opcional): mostra o cálculo do fatorial se o valor for `True`
    return: Retorna o valor do fatorial de `n`
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
