
from datetime import date

menoridade = 0
maioridade = 0

for person in range(1, 8):
    current_year = date.today().year
    nasc = int(input('Ano de nascimento da {}ª pessoa: '.format(person)))
    age = current_year - nasc
    if age >= 18:
        maioridade += 1
    if age <= 18:
        menoridade += 1

print('No grupo informado,\n{} pessoas atingiram a maioridade\n{} pessoas estão na menoridade.'.format(maioridade, menoridade))
