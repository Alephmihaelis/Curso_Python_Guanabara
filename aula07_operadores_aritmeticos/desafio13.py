
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

colors = {
    'green': '\033[32m',
    'under': '\033[4m',
    'limpa': '\033[m'
}

salario = float(input('Salário do funcionário: R$'))

print('{}{}Com 15% de aumento, o salário do funcionário, que é de R${:.2f}, passará a ser \nR${:.2f}{}\n"AAAAAAAAAAAAAAAA"'.format(
    colors['green'],
    colors['under'],
    salario,
    salario + (salario * 15/100),
    colors['limpa']
    ))

# Continuo evitando o uso desnecessário de variáveis, uma vez que o resultado é exibido uma vez só.
# Este `"AAAAAAAAAAAAAAAA"` foi um teste; aparentemente, basta fechar o comando uma só vez.
