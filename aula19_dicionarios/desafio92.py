
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
print('=' * 30)

ano = date.today().year

pessoa = {}

pessoa['nome'] = input('NOME: ')
nascimento = int(input('ANO DE NASCIMENTO: '))
pessoa['idade'] = ano - nascimento
pessoa['ctps'] = int(input('NÚMERO DA CARTEIRA DE TRABALHO [0 se não existe]: '))

if pessoa['ctps'] != 0:
    pessoa['ano_de_contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    pessoa['salário'] = int(input('QUAL SEU SALÁRIO? R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['ano_de_contratação'] + 35) - ano

    print('~' * 30)
    
for k, v in pessoa.items():
    print(f'{k.upper()} = {v}')
