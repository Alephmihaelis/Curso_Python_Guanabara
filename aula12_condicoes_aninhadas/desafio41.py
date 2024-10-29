
# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: 1. Até 9 anos: MIRIM; 2. Até 14 anos: INFANTIL; Até 19 anos: JÚNIOR; Até 20 anos: SÊNIOR; Acima: MASTER.

from datetime import date

current_year = date.today().year

print('=*='*11)
print('Divisão de categoria de atletas')
print('=*='*11)

birth = int(input('Ano de nascimento: '))
age = current_year - birth

if age <= 9:
    print('Idade do atleta: {} anos\nCLASSIFICAÇÃO: Mirim'.format(age))
elif age <= 14:
    print('Idade do atleta: {} anos\nCLASSIFICAÇÃO: Infantil'.format(age))
elif age <= 19:
    print('Idade do atleta: {} anos\nCLASSIFICAÇÃO: Júnior'.format(age))
elif age <= 20:
    print('Idade do atleta: {} anos\nCLASSIFICAÇÃO: Sênior'.format(age))
else:
    print('Idade do atleta: {} anos\nCLASSIFICAÇÃO: Master'.format(age))
