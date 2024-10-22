
# Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

# Resolução em que pensei.

alunos = 'Álefe', 'Gisele', 'Pedro', 'João'
print('O aluno escolhido foi {}!'.format(choice(alunos)))

# O professor nomeou os alunos com `input`

aluno_um = input('Primeiro aluno: ')
aluno_dois = input('Segundo aluno: ')
aluno_tres = input('Terceiro aluno: ')
aluno_quatro = input('Quatro alunos: ')

# O professor cria uma `lista`. Listas são representadas por `[]`.

# Criação da lista
lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
print('O aluno escolhido foi {}!'.format(choice(lista_alunos)))
