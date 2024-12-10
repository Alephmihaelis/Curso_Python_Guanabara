
def moedas(valor):
    res = f'R${valor:.2f}'.replace(".", ",")
    return res


def aumentar(n = 0, valor=0):
    soma = n + valor
    return moedas(soma)
    
    
def diminuir(valor = 0, n=0):
    subtracao = valor - n
    return moedas(subtracao)
    
    
def dobro(valor = 0):
    dobro = valor * 2
    return moedas(dobro)
    
    
def metade(valor = 0):
    metade = valor / 2
    return moedas(metade)


