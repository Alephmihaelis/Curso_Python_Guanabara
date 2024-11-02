
# Crie um programa que leia o ano do nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

# Recebe o ano atual do computador
ano_atual = date.today().year

# Acumuladores
menoridade = 0
maioridade = 0

# `Loop` em que se leem sete datas de nascimento
for data in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(data)))
    
    # Variável que calcular a idade
    idade = ano_atual - nascimento

    # Acrescenta 1 à variável `menoridade`, se a idade for menor que 18 anos
    if idade < 18:
        menoridade += 1

    # Acrescenta 1 à variável `maioridade`, se a idade for maior que 18 anos, ou igual a 18 anos.
    elif idade >= 18:
        maioridade += 1

print('No grupo das pessoas citadas:\n{} já atingiram a maioridade;\n{} têm menos de 18 anos.'.format(maioridade, menoridade))
