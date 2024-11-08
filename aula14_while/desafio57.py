
'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

colors = {
    'bold': '\033[1m',
    'red': '\033[31m',
    'limpa': '\033[m'
}

print('='*27)
print('PEQUENA VALIDAÇÃO DE DADOS')
print('='*27)

sexo = input('Informe seu sexo [M/F]: ').upper()

while sexo not in 'MF':
    print('Resposta inválida.')
    print('-='*20)
    sexo = input('Informe seu sexo: [M/F]: ').upper()
if sexo == 'M':
    print('{}Você foi registrado com sucesso!{}'.format(colors['bold'], colors['limpa']))
elif sexo == 'F':
    print('{}Você foi registrada com sucesso!{}'.format(colors['red'], colors['limpa']))
