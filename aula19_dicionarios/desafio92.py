
'''
Crie um programa que leia `nome`, `ano de nascimento` e `carteira de trabalho` de uma pessoa,
e cadastre com a idade em um dicionário.
Se a CTPS for diferente de zero, o dicionário receberá
também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
A pessoa se aposenta depois de 35 anos de colaboração.
'''

from datetime import date

print('=' * 30)
print('ANÁLISE DE CTPS!')
print('Se você não tem CTPS,\ndigite 0 quando lhe for perguntado o número da CTPS.')
print('=' * 30)

ano = date.today().year

pessoa = {}

pessoa['nome'] = input('NOME: ')
nascimento = int(input('ANO DE NASCIMENTO: '))
pessoa['idade'] = ano - nascimento
pessoa['cpts'] = int(input('NÚMERO DA CARTEIRA DE TRABALHO: '))

if pessoa['cpts'] != 0:
    pessoa['ano_de_contratacao'] = int(input('EM QUE ANO VOCÊ FOI CONTRATADO(A)? '))
    pessoa['salario'] = int(input('QUANTO VOCÊ RECEBE? R$'))
    print(f'ANO MÍNIMO PARA SE APOSENTAR: {pessoa["ano_de_contratacao"] + 35}')

elif pessoa['cpts'] == 0:
    print('Você ainda não tem carteira de trabalho!')
