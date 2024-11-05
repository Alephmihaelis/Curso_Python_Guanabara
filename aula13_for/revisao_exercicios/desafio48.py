
# Inicia a variável `soma` com valor 0. É o acumulador
soma = 0

# Inicia a variável `impar` com valor 0. É o contador
impar = 0

# `Loop` que percorre o intervalo entre 1 e 501
for impares in range(1, 501, 2):
    # Verifica se o valor de `impares` é múltiplo de 3
    if impares % 3 == 0:
        print(impares)

        # Se sim, soma esse número à soma 
        soma = soma + impares

        # Se sim, soma 1 a cada número múltiplo de 3
        impar += 1

print('No intervalo informado, há {} números múltiplos de 3'.format(impar))
print('A soma de todos esses números é {}'.format(soma))
