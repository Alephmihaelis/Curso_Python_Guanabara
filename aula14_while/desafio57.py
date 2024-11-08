
'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = input('Qual seu sexo? [M/F]: ').upper().strip()[0]

while sexo not in ['M', 'F']:
    print('Dados inválidos. Por favor, tente novamente.')
    sexo = input('Qual seu sexo? [M/F]: ').upper().strip()[0]

if sexo == 'M':
        print('Registrado com sucesso.')
if sexo == 'F':
        print('Registrada com sucesso.')
