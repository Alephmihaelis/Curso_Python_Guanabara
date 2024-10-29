
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: 1. Media abaixo de 5.0: REPROVADO; 2. Média entre 5.0 e 6.9: RECUPERAÇÃO; 3. Média 7.0 ou superior: APROVADO.

colors = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'limpa': '\033[m'
}

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2

if media < 5:
    print('Média do aluno: {:.1f}\n{}REPROVADO!{}'.format(media,
                                                          colors['red'],
                                                          colors['limpa']))
elif media > 5 and media <= 6.9:
    print('Média do aluno: {:.1f}\n{}RECUPERAÇÃO!{}'.format(media,
                                                        colors['yellow'],
                                                        colors['limpa']))
else:
    print('Média do aluno: {:.1f}\n{}APROVADO!{}'.format(media,
                                                         colors['green'],
                                                         colors['limpa']))
