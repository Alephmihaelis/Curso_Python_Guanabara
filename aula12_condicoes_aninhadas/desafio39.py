
# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: 1. Se ele ainda se alistará no serviço militar; 2. Se é a hora de se alistar; 3. Se já passou do tempo do alistamento. O programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

text = {
    'bold': '\033[1m',
    'red': '\033[31m',
    'limpa': '\033[m'
}

current_year = date.today().year # Também posso obter o ano atual do computador com
                                 # `datetime.datetime.now().year`

print('-='*20)
print('Alistamento militar obrigatório')
print('-='*20)

print('Em primeiro lugar, verificaremos se você é {}homem{} ou {}mulher{}.'.format(
    text['bold'],
    text['limpa'],
    text['bold'],
    text['limpa']
    ))

sex = input('''Você é homem ou mulher?
Digite [H] para HOMEM
Digite [M] para MULHER
Resposta: ''').upper()

if sex == 'H':

    year = int(input('Ano de nascimento: '))
    age = current_year - year
    print('Quem nasceu em {} tem {} anos em {}.'.format(
    year,
    age,
    current_year
    ))
    
    if age < 18:
        print('Já que você ainda não tem 18 anos, ainda não é hora de alistar-se.\nVocê deverá se alistar daqui a {} anos.\nSeu alistamento deverá ocorrer em {}.'.format(
        18 - age,
        year + 18
    ))
    
    elif age == 18:
        print('Você {}deve se alistar imediatamente!{}'.format(
        text['bold'],
        text['limpa']
    ))
        
    elif age > 18:
        print('Já passou a hora de alistar-se!\nVocê está atrasado {} anos.\nSeu alistamento foi em {}.'.format(
        age - 18,
        year + 18
    ))

elif sex == 'M':
    print('{}{}O alistamento militar brasileiro não é obrigatório para mulheres.{}'.format(
        text['bold'],
        text['red'],
        text['limpa']
                    ))

else:
    print('Resposta inválida.')
