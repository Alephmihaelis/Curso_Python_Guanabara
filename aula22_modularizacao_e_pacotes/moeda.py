

def moedas(valor, fmt=False):
    n_format = f'R${valor}'
    if fmt:
        res = f'R${valor:.2f}'.replace(".", ",")
        return res
    else:
        return n_format


def aumentar(n = 0, valor=0, fmt=False):
    soma = n + valor
    return moedas(soma, fmt)
    
    
def diminuir(valor = 0, n=0, fmt=False):
    subtracao = valor - n
    return moedas(subtracao, fmt)
    
    
def dobro(valor = 0, fmt=False):
    dobro = valor * 2
    return moedas(dobro, fmt)
    
    
def metade(valor = 0, fmt=False):
    metade = valor / 2
    return moedas(metade, fmt)


