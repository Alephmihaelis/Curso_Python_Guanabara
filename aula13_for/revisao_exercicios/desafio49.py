
# Importa a função `sleep` da biblioteca `time`
from time import sleep

# Pede que o usuário informe um número
num = int(input('Informe um número para ver-lhe a tabuada: '))

# Mostra a string na tela, para simular um cálculo
print('\033[31mCalculando...\033[m')

# Complemento da simulação do cálculo, em que o computador espera 1 segundo antes de mostrar o resultado
sleep(1)

# `Loop` que percorre o intervalo de 1 a 10, para multiplicar o número informado pelo usuário por cada número recebido em `x`
for x in range(1, 11):
    # Mostra a tabuada
    print('{} x {} = {}'.format(num, x, num*x))
