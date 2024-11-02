
# Crie um programa que leia o ano do nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

# Recebe o ano atual do computador
ano_atual = date.today().year

# Contadores
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
    else:
        maioridade += 1

# Tratamento da string para casos singulares e plurais
if menoridade == 1 and maioridade > 1:
    print('No grupo das pessoas citadas, \n{} pessoas atingiram a maioridade\n{} pessoa ainda não atingiu a maioridade'.format(maioridade, menoridade))
elif maioridade == 1 and menoridade > 1:
    print('No grupo das pessoas citadas, \n{} pessoa atingiu a maioridade\n{} pessoas ainda não atingiram a maioridade'.format(maioridade, menoridade))