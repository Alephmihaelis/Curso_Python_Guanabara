
'''
Desenvolva um programa que leia o nome, a idade e o sexo de quatro pessoas.
No final, mostre:
1. a média de idade do grupo;
2. qual o nome do homem mais velho;
3. quantas mulheres têm menos de 21 anos.
'''

from sys import exit

# Variável para soma das idades. É o acumulador.
idade_tot = 0

# Variável para contar quantos homens há no grupo
homem = 0

# Variável para contar quantas mulheres há no grupo
mulher = 0

# Variável para armazenar o nome do homem mais velho
h_mais_velho = ''

# Variável para armazenar a idade do homem mais velho
idade_h_mais_velho = 0

# Variável para armazenar quantas mulheres no grupo têm menos de 21 anos
menos_21 = 0

# `Loop` em que se coletam informações de quatro pessoas
for pessoas in range(1,5):
    print('----- {}ª PESSOA -----'.format(pessoas))

    # Coleta o nome
    nome = input('Nome: ').strip()
    
    # Coleta a idade
    idade = int(input('Idade: '))

    # Coleta a idade total do grupo
    idade_tot += idade

    # Calcula a média de idade do grupo
    media_idade = idade_tot / 4

    # Coleta o sexo do integrande do grupo, e converte a resposta para maiúscula
    sex = input('Sexo [M]/[F]: ').upper().strip()

    # Verifica se a resposta à variável `sex` é válida. Se não for, encerra o programa
    if sex not in ['M', 'F']:
        print('Resposta inválida! Tente novamente.')
        exit()
    
    # Se a variável `sex` for 'M':
    elif sex == 'M':
        # Insere um homem na contagem
        homem += 1

        # Verifica se a idade atual é maior que a do homem mais velho
        if idade > idade_h_mais_velho:

            # Se for, `idade` passa a ser `idade_h_mais velho`
            idade_h_mais_velho = idade

            # Coleta o nome do homem mais velho
            h_mais_velho = nome

    # Se `sex` for 'F':
    elif sex == 'F':

        # Insere uma mulher
        mulher += 1

        # Verifica quantas mulheres têm menos de 21 anos
        if idade < 21:
            menos_21 += 1

    print('------------------------------')


print('Média de idade do grupo: {} anos'.format(media_idade))
print('Quantidade de homens no grupo: {}'.format(homem))
print('Quantidade de mulheres no grupo: {}'.format(mulher))
print('Nome do homem mais velho e sua idade: {}, {} anos'.format(h_mais_velho, idade_h_mais_velho))
print('Quantas mulheres têm menos de 21 anos? {}'.format(menos_21))