def moedas(valor):
    res = f'R${valor:.2f}'
    return res


def aumentar(n, valor=0):
    soma = n + valor
    return moedas(soma)
    
    
def diminuir(valor, n=0):
    subtracao = valor - n
    return moedas(subtracao)
    
    
def dobro(valor):
    dobro = valor * 2
    return moedas(dobro)
    
    
def metade(valor):
    metade = valor / 2
    return moedas(metade)


