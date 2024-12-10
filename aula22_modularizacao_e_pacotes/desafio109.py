
'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

from moeda import diminuir

num = float(input('Digite um valor em reais: '))
valor = float(input('Quanto você quer subtrair? '))
print('Valor total: ', end='')
print(diminuir(num, valor, True))

'''
Não fiz este desafio, porque a solução que gerei para os meus módulos já "matava" o problema apontado pelo professor.

Por outro lado, eu poderia escrever a função que formata a saída de dados da seguinte maneira:
def moedas(valor, fmt=False):
    n_format = f'R${valor}'
    if format:
        res = f'R${valor:.2f}'.replace(".", ",")
        return res
    else:
        return n_format

No fim, essa ficou sendo a função final.
        
'''