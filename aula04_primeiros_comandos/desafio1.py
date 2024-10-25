print('-=-'*15)
print('\033[1;33;45mOlá, mundo! Estou aprendendo Python!\033[m')
print('-=-'*15)

nome = input('\033[4;32mQual seu nome?\033[m ')
print('Olá, ' + nome + '! É um prazer te conhecer!')

nome2 = input('\033[1mQual seu nome?\033[m ')
print('Olá, \033[1;32m{}\033[m! É um prazer conhecer você. :D'.format(nome2))