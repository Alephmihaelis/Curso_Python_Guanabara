
'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

#OBS.: te programa ainda não está pronto; há erros nele.

from random import randint

jogada_pc = randint(1,10)

vitoria = 0

print('~'*20)
print('PAR OU ÍMPAR!')
print('~'*20)

while True:

    jogador_par_impar = input('Você quer PAR ou ÍMPAR? [P/I]: ').upper()
    jogador = int(input('Sua jogada: '))

    if jogador_par_impar == 'P':
        print(f'Computador jogou {jogada_pc}')
        if (jogador + jogada_pc) % 2 == 0:
            print('Você venceu! Parabéns!')
            vitoria += 1
        elif (jogador + jogada_pc) % 2 < 0:
            print('Que pena! Você perdeu!')
            break
    
    if jogador_par_impar == 'I':
        print(f'Computador jogou {jogada_pc}')
        if (jogador + jogada_pc) % 2 == 0:
            print('Que pena! Você perdeu!')
            break
        elif (jogador + jogada_pc) % 2 < 0:
            print('Parabéns, você venceu!')
            vitoria += 1

print(f'Você venceu {vitoria} vezes.')
