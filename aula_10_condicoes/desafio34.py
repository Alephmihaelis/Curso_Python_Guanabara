
'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250.00, calcule um aumento de 10%.
Para salários inferiores ou iguais a isso, calcule um aumento de 15%.
'''

salary = float(input('Salário do funcionário: R$'))

if salary > 1250:
    aumento = salary*(10/100)

else:
    aumento = salary*(15/100)

new_salary = salary+aumento

print('O salário do funcionário aumentou R${:.2f}\nO novo salário do funcionário será R${:.2f}'.format(
    aumento,
    new_salary
    ))
