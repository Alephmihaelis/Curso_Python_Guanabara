
from modulos23 import interface, arquivo
from time import sleep

arq = 'lista.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
       arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.cabecalho('Saindo do sistema... Até mais!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
