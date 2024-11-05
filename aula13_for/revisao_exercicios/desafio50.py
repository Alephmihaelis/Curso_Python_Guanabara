
# Contador para os números pares, começando com 0
pares = 0

# Acumulador para os números pares, começando com 0
soma_pares = 0

# `Loop` que pede seis vezes um número ao usuário
for vezes in range(1, 7):
    num_user = int(input('Digite um número: '))

    # Estrutura condicional que verifica se os números são pares
    if num_user % 2 == 0:

        # Conta quantos pares foram informados
        pares += 1

        # Se os números passarem pela estrutura condicional, soma os pares
        soma_pares += num_user

# Imprime a soma dos números
print('{} números pares foram informados.\nA soma de todos os números pares vale {}'.format(
    pares,
    soma_pares
    ))
