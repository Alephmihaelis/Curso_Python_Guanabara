
'''
Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário, e todos os dicionários em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas;
b) A média de idade do grupo;
c) Uma lista com todas as mulheres;
d) Uma lista com todas as pessoas com idade acima da média.
'''

galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Dado inválido.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Deseja continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Dado inválido.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Total de pessoas cadastradas: {len(galera)}')
print(f'Média de idade: {soma / len(galera):.2f}')
print(f'As mulheres cadastradas foram ', end='')

for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')

print('\nLista das pessoas que estão acima da média de idade do grupo: ', end='')
for p in galera:
    if p['idade'] >= soma / len(galera):
        print('        ', end='')
        for k, v in p.items():
            print(f'{k}, {v}; ', end='')
        print()
print('<< ENCERRADO >>')
