
'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'Santo'
'''

city_name = input('Nome da cidade: ').strip().title()
print('A cidade digitada foi "{}".\nEla começa com "Santo"? {}'.format(
    city_name,
    'Santo' in city_name.split()[0]
))

# Meu código foi um pouco diferente do do professor. Usei o operador `in`.
