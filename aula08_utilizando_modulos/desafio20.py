
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

aluno_um = input('Primeiro aluno: ')
aluno_dois = input('Segundo aluno: ')
aluno_tres = input('Terceiro aluno: ')
aluno_quatro = input('Quarto aluno: ')

alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]

print('A ordem de apresentação será:\n{}'.format(
    sample(alunos, k=4)
    ))

# O professor usou `random.shuffle(...)`; mas eu resolvi o exercício com `sample`.
