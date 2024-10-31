
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

colors = {
    'red': '\033[31m',
    'green': '\033[32m',
    'limpa': '\033[m'
}

print('='*22)
print('Vamos jogar `Jokenpô`!')
print('='*22)

jogadas = ['Pedra', 'Papel', 'Tesoura'] # O professor pôs as opções entre (); eu as pus entre [].

jogada_pc = choice(jogadas) # O professor usou só `randint`; eu, apenas `choice`

# Escolha do jogador
jogador = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\nJogada: '))

if jogador not in [0, 1, 2]:
    print('Jogada inválida! Tente novamente.')

elif jogador in [0, 1, 2]:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        
        print('='*30)
        jogada_jogador = jogadas[jogador]
        print('Jogador jogou {}\nComputador jogou {}'.format(
        jogada_jogador,
        jogada_pc
    ))
        print('='*30)
        if jogada_jogador == 'Pedra':
            if jogada_pc == 'Papel':
                print('{}Computador venceu!{}'.format(colors['green'], colors['limpa']))
            elif jogada_pc == 'Tesoura':
                print('{}Jogador venceu!{}'.format(colors['green'], colors['limpa']))
            elif jogada_pc == jogada_jogador:
                print('{}Empate!{}'.format(colors['red'], colors['limpa']))
        
        elif jogada_jogador == 'Papel':
            if jogada_pc == 'Pedra':
                print('{}Jogador venceu!{}'.format(colors['green'], colors['limpa']))
            elif jogada_pc == 'Tesoura':
                print('{}Computador venceu!{}'.format(colors['green'], colors['limpa']))
            elif jogada_pc == jogada_jogador:
                print('{}Empate!{}'.format(colors['red'], colors['limpa']))
        
        elif jogada_jogador == 'Tesoura':
            if jogada_pc == 'Pedra':
                print('{}Computador venceu!{}'.format(colors['green'], colors['limpa']))
            elif jogada_pc == 'Papel':
                print('{}Jogador venceu!{}'.format(colors['green'], colors['limpa']))
            elif jogada_pc == jogada_jogador:
                print('{}Empate!{}'.format(colors['red'], colors['limpa']))
