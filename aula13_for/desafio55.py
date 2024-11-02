
# Faça um programa que leia o peso de 5 pessoas e no final mostre qual foi o maior e o menor peso lidos.

maior = 0

# Atribuí o valor `500` à variável menor, para que possa ser comparada dentro do `loop`. O valor `500` foi escolhido, porque não me era possível atribuir o valor `0` a essa variável. Tentei inicialmente passar o valor `None`, mas `None` não é compatível com o operador.
menor = 500

# O professor, porém, ensinou uma técnica para burlar essa atribuição alta:

'''
for pesos in range(1,6):
    peso = float(input('{}º peso: '.format(pesos)))
    if pesos == 1:
        maior = peso
        menor = peso
        '''

for pesos in range(1, 6):
    peso = float(input('{}º peso: '.format(pesos)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso foi {}kg\nO menor peso foi {}kg'.format(maior, menor))
