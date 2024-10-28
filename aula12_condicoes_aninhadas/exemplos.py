
nome = input('Qual é seu nome? ').strip().capitalize()

if nome == 'Bob o bobo':
    print('Que nome legal!')
elif nome == 'Trocatapas' or nome == 'Crueza' or nome == 'Pedrin':
    print('Que doido esse seu nome!')
elif nome in ['Ana', 'Josefina', 'Tobi']:
    print('Sabe muito!')
else:
    print('Seu nome é tão normal...')

print('Tenha um bom dia, {}!'.format(
    nome
))
