
numeros = (int(input('Primeiro valor: ')),
           int(input('Segundo valor: ')),
           int(input('Terceiro valor: ')),
           int(input('Quarto valor: ')))

if 9 in numeros:
    print(f'O número 9 apareceu {numeros.count(9)} vezes')
else:
    print('O número 9 não foi digitado.')

if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado.')

print(f'Os números pares digitados foram ', end='')

for n in numeros:
    if n % 2 == 0:
        print(n, end = ' ')

# Eu poderia tratar melhor o plural dos números pares, mas aqui não é tão necessário.
