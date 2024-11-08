
# Contador de divisores
divisor = 0

# Pede que o usuário informe um número, e converte esse número para número inteiro
num = int(input('Digite um número: '))

# `Loop` que vai de 1 até o número informado pelo usuário
for x in range(1, num+1):

    # Verifica se a divisão de `num` é igual a 0, segundo os números do `loop`
    if num % x == 0:
        print('\033[33m{}\033[m'.format(x), end=' ')

        # Se a condição for verdadeira, acrescenta 1 ao divisor
        divisor += 1

    # Se o resto da divisão for diferente de 0, põe esses divisores em vermelho
    if num % x != 0:
        print('\033[31m{}\033[m'.format(x), end=' ')

# Se houver mais que dois divisores, mostra que não é primo
if divisor > 2:
    print('\nO número {} é \033[33mdivisível\033[m {} vezes.\nPortanto, ele não é primo.'.format(num, divisor))

# Se o valor de `divisor` for igual a dois, mostra que o número é primo
if divisor == 2:
    print('\nO número {} é \033[31mdivisível\033[m somente {} vezes.\nPortanto, ele é primo.'.format(num, divisor))
