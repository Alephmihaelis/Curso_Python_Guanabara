
m_dezoito, homens, m_n_vinte = 0, 0, 0

print('~'*20)
print('CADASTRO DE PESSOAS')
print('~'*20)

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    print('-'*20)

    if sexo not in 'MF':
        print('Opção inválida. Tente novamente.')
        sexo = input('Sexo [M/F]: ').upper().strip()
    
    if idade > 18:
        m_dezoito += 1
    
    if sexo == 'M':
        homens += 1
    
    if sexo == 'F':
        if idade < 20:
            m_n_vinte += 1

    question = ' '
    while question not in 'SN':
        question = input('Deseja continuar? [S/N] ').upper().strip()
    if question == 'N':
        break
    print('-'*20)

if m_dezoito > 1:
    print(f'{m_dezoito} pessoas têm mais de 18 anos.')
elif m_dezoito == 1:
    print('Somente uma das pessoas cadastradas têm mais de 18 anos.')
elif m_dezoito == 0:
    print('Nenhuma das pessoas cadastradas tem mais de 18 anos.')

if homens > 1:
    print(f'{homens} homens foram cadastrados.')
elif homens == 1:
    print('Somente um homem foi cadastrado.')
elif homens == 0:
    print('Nenhum homem foi cadastrado.')

if m_n_vinte > 1:
    print(f'{m_n_vinte} mulheres têm menos de 20 anos.')
elif m_n_vinte == 1:
    print('Somente uma das mulheres cadastradas tem menos de 20 anos.')
elif m_n_vinte == 0:
    print('Nenhuma mulher cadastrada tem menos de 20 anos.')
