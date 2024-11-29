
'''
Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
Média >= 7: APROVADO
Média <= 7: REPROVADO
'''

dicionario = {
    'nome': '',
    'média': float,
    'situação': ''
}

print('~' * 30)
nome = input('Nome do aluno: ')
dicionario['nome'] = nome

media = float(input('Média do aluno: '))
dicionario['média'] = media

if media >= 7:
    dicionario['situação'] = 'Aprovado'
else:
    dicionario['situação'] = 'Reprovado'

print('~' * 30)

for k, v in dicionario.items():
    print(f'{k.upper()}: {v}')
