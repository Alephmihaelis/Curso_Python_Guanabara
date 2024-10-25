
print('\033[0;30;41mExemplo 1\033[m')
print('\033[4;33;44mExemplo 2\033[m')
print('\033[1;35;43mExemplo 3\033[m')
print('\033[0;30;42mExemplo 4\033[m')
print('\033[mExemplo 4\033')
print('\033[7;30mExemplo 5\033[m')

colors = {
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'vermelho': '\033[31m',
    'bold': '\033[1m',
    'limpa': '\033[m'
}

print('{}— E aí Tudo bem?\n{}{}— Tudo bem, meu amigo!{}\n{}— Oi, pessoal! Cheguei!{}\n{}— Bem, parece que estão todos aqui...{}'.format(
    colors['amarelo'],
    colors['limpa'],
    colors['azul'],
    colors['limpa'],
    colors['vermelho'],
    colors['limpa'],
    colors['bold'],
    colors['limpa']
    ))
