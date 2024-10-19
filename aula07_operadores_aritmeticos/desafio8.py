
# Escreva um programa que leia um valor em metros e o exiba convertido em outras unidades de comprimento.

alpha = float(input('Digite um valor em metros: '))
print('Analisando o valor informado, percebe-se que:\n{}m equivale(m) a {}km\n{}m equivale(m) a {}hm\n{}m equivale(m) a {}dam\n{}m equivale(m) a {:.0f}dm\n{}m equivale(m) a {:.0f}cm\n{}m equivale(m) a {:.0f}mm'.format(alpha, (alpha/1000), alpha, (alpha/100), alpha, (alpha/10), alpha, (alpha*10), alpha, (alpha*100), alpha, (alpha*1000)))

# Ao depois procurarei maneiras de tornar este código mais legível.