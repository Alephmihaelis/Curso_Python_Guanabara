
'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguido o primeiro e último nome separadamente.
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

name = input('Nome completo: ').strip()
print('Olá, {}!\nSEU PRIMEIRO NOME: {}\nSEU ÚLTIMO NOME: {}'.format(
    name,
    name.split()[0],
    name.split()[-1]
))

# Minha solução foi um pouco diferente da do professor, que usou a função `len`. Eu simplesmente fiz um fatiamento com os itens da lista.
