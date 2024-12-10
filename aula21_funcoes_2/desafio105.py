
'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''

def notas(* n, sit=False):
    '''
    Função para analisar notas e funções de vários alunos
    `n`: uma ou mais notas dos alunos (aceita várias notas)
    `sit`: valor opcional que mostra a situação da turma de acordo com as notas informadas
    '''

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'

    return r


resposta = notas(5.5, 2.5, 6, sit=True)
print(resposta)
