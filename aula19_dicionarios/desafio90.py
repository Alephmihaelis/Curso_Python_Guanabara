
'''
Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
Média >= 7: APROVADO
Média <= 7: REPROVADO
'''

aluno = {
    'nome': str,
    'média': float,
    'situação': str
}

print('~' * 30)
nome = input('Nome do aluno: ')
aluno['nome'] = nome

media = float(input('Média do aluno: '))
aluno['média'] = media

if media >= 7:
    aluno['situação'] = 'Aprovado'
elif media >= 5 and media < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('~' * 30)

for k, v in aluno.items():
    print(f'{k.upper()}: {v}')
