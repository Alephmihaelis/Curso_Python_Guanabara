
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

alpha = float(input('Digite a primeira nota: '))
beta = float(input('Digite a segunda nota: '))

print('As notas do aluno são {} e {}.\nA média do aluno é {:.1f}'.format(alpha, beta, (alpha + beta) / 2))
