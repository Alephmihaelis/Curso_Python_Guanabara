
'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#OBS.: te programa ainda não está pronto; há erros nele.
'''

from random import randint

# Número que o computador escolherá aleatoriamente
jogada_pc = randint(1,10)

# Contador de vitórias do jogador
vitoria = 0

print('~'*20)
print('PAR OU ÍMPAR!')
print('~'*20)

while True:

    # Pede que o jogador escolha um número
    jogador = int(input('Sua jogada: '))

    # Pergunta se o jogador quer "par" ou "ímpar"
    jogador_par_impar = input('Você jogará PAR ou ÍMPAR? [P/I]: ').upper()

    if jogador_par_impar == 'P':
        print(f'Você jogou {jogador}\nComputador jogou {jogada_pc}')
        if (jogador + jogada_pc) % 2 == 0:
            print('Você venceu! Parabéns!')
            vitoria += 1
        if (jogador + jogada_pc) % 2 != 0:
            print('Que pena! Você perdeu!')
            break
    
    if jogador_par_impar == 'I':
        print(f'Você jogou {jogador}\nComputador jogou {jogada_pc}')
        if (jogador + jogada_pc) % 2 == 0:
            print('Que pena! Você perdeu!')
            break
        if (jogador + jogada_pc) % 2 != 0:
            print('Parabéns, você venceu!')
            vitoria += 1

if vitoria > 1:
    print(f'Você venceu {vitoria} vezes.')

if vitoria == 1:
    print(f'Você venceu {vitoria} uma vez')

if vitoria == 0:
    print('Você não venceu nenhuma vez!')