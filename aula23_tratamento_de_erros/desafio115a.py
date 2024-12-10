
'''
Acesso a arquivos usando Python.
'''

from modulos23 import interface
from time import sleep

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        interface.cabecalho('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        interface.cabecalho('Saindo do sistema... Até mais!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
    