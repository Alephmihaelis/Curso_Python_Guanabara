
'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''

def voto(nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade < 16:
        return f'Você tem {idade} anos.\nSITUAÇÃO: Voto NEGADO.'
    elif idade >= 16 and idade < 65:
        return f'Você tem {idade} anos.\nSITUAÇÃO: Voto OBRIGATÓRIO.'
    else:
        return f'Você tem {idade} anos. \nSITUAÇÃO: Voto OPCIONAL.'

ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))