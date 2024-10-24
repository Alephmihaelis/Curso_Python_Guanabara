
'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1. O nome com todas as letras maiúsculas;
2. O nome com todas as letra minúsculas;
3. Quantas letras ao todo (sem considerar espaços);
4. Quantas letras tem o primeiro nome.
'''

name = str(input('Digite um nome completo: ')).strip()
n_maisculas = name.upper()
n_minusculas = name.lower()
no_spaces = name.count(' ')
first_name = name.split()

print('MAIÚSCULAS: {}\nMINÚSCULAS: {}\nSEM ESPAÇOS: {}\nQUANTIDADE DE LETRAS DO PRIMEIRO NOME: {}'.format(
    n_maisculas,
    n_minusculas,
    len(name) - no_spaces,
    name.find(' '))
)

# Resolvi usar variáveis, pois com elas o código ficou mais limpo.