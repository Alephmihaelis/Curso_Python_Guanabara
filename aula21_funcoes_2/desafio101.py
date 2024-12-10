
'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''

def voto(nasc):
    from datetime import date
    idade = ano_atual - ano_nasc
    ano_atual = date.today().year

    if idade < 18:
        print(f'Você tem {idade} anos.\nSITUAÇÃO: Voto NEGADO.')
    elif idade >= 18 and idade < 65:
        print(f'Você tem {idade} anos.\nSITUAÇÃO: Voto OBRIGATÓRIO.')
    else:
        print(f'Você tem {idade} anos. \nSITUAÇÃO: Voto OPCIONAL.')

ano_nasc = int(input('Em que ano você nasceu? '))

voto(ano_nasc)