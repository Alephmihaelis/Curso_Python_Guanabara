
"""
Programa que sorteia
um alunos para apagar o quadro;
lê o nome de algunos e escreve o nome do escolhido.
"""

from random import choice

alunos = 'Bob', 'Paty', 'Poo', 'Goku'
print('O aluno escolhido foi {}!'.format(choice(alunos)))

# O professor nomeou os alunos com `input`

aluno_um = input('Primeiro aluno: ').strip()
aluno_dois = input('Segundo aluno: ').strip()
aluno_tres = input('Terceiro aluno: ').strip()
aluno_quatro = input('Quatro alunos: ').strip()

lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
print('O aluno escolhido foi {}!'.format(choice(lista_alunos)))
