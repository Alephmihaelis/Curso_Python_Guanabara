
# Começa as variáveis
idades = 0 # Será usada para calcular o total da idade do grupo
m_velho = '' # Armazenará o nome do homem mais velho
idade_m_velho = 0 # Armazenará a idade do homem mais velho

# Coleta as informações de quatro pessoas
for person in range(1, 5):

    name = input('Nome da {}ª pessoa: '.format(person))
    idade = int(input('Idade da {}ª pessoa: '.format(person)))
    sexo = input('Sexo da {}ª pessoa: [M] = Masculino\n[F] = Feminino: '.format(person)).upper()
    
    idades += idade

    if sexo == 'M':
        if idade > idade_m_velho:
            idade_m_velho = idade
            m_velho = name

media_idade = idades / 4

print('A média de idade do grupo é {} anos'.format(media_idade))
print('A idade do homem mais velho é {} anos'.format(idade_m_velho))
print('O nome do homem mais velho {}.'.format(m_velho))