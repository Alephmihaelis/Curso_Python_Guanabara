
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('\033[7;32;41mA soma entre {} e {} vale {}\033[m'.format(
    n1,
    n2,
    s
    ))