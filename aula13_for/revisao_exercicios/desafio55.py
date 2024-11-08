
menor = 0
maior = 0

for person in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(person)))
    if person == 1:
        menor = peso
        maior = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))
