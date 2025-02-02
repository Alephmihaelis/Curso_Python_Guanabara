
"""
Algoritmo que lê o salário de um funcionário
e mostra seu novo salário, com 15% de aumento.
"""

colors = {
    'green': '\033[32m',
    'under': '\033[4m',
    'limpa': '\033[m'
}

print('Salário do funcionário: R$')
salario = float(input())

print('{}{}Com 15% de aumento, o salário do funcionário, que é de R${:.2f}, passará a ser\nR${:.2f}{}'.format(
    colors['green'],
    colors['under'],
    salario,
    salario + (salario * 15/100),
    colors['limpa']
    ))
