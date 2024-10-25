
# Escreva um programa que leia um valor em metros e o exiba convertido em outras unidades de comprimento.

alpha = float(input('Digite um valor em metros: '))
print('Analisando o valor informado, percebe-se que:\n\033[31m{}m\033[m equivale(m) a \033[32m{}km\033[m\n\033[33m{}m\033[m equivale(m) a \033[34m{}hm\033[m\n\033[35m{}m\033[m equivale(m) a \033[36m{}dam\033[m\n{}m equivale(m) a \033[37m{:.0f}dm\033[m\n{}m equivale(m) a {:.0f}cm\n{}m equivale(m) a {:.0f}mm'.format(
    alpha,
    (alpha/1000),
    alpha,
    (alpha/100),
    alpha,
    (alpha/10),
    alpha,
    (alpha*10),
    alpha,
    (alpha*100),
    alpha,
    (alpha*1000)
    ))

# Ao depois procurarei maneiras de tornar este código mais legível.