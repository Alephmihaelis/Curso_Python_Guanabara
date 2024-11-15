from random import randint

vitoria = 0

print('~'*20)
print('PAR OU ÍMPAR!')
print('~'*20)

while True:

    pc = randint(1, 10)
    jogador = int(input('Jogada: '))
    par_impar = input('PAR ou ÍMPAR? [P/I]: ').upper().strip()

    while par_impar not in 'PI':
        print('Escolha inválida. Tente novamente.')
        par_impar = input('PAR ou ÍMPAR? [P/I]: ').upper().strip()

    print('=-'*22)
    print(f'Você jogou {jogador}\nComputador jogou {pc}')
    print('=-'*22)

    if par_impar == 'P':
        if (jogador + pc) % 2 == 0:
            print('Você venceu! Parabéns!\nJoguemos novamente!')
            vitoria += 1

        elif (jogador + pc) % 2 != 0:
            print('Que pena! Você perdeu!')
            break

    if par_impar == 'I':
        if (jogador + pc) % 2 == 0:
            print('Que pena! Você perdeu!')
            break
        
        elif (jogador + pc) % 2 != 0:
            print('Parabéns, você venceu!\nJoguemos novamente!')
            vitoria += 1
    print('~'*20)

if vitoria > 1:
    print(f'Ao todo, você venceu {vitoria} vezes.')

if vitoria == 1:
    print(f'Ao todo, você só venceu {vitoria} uma vez')

if vitoria == 0:
    print('Que dó! Você não venceu nenhuma vez!')
