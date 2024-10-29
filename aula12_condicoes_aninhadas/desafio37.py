
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão: [1] para binário; [2] para octal; [3] para hexadecimal.

text = {
    'bold': '\033[1m',
    'yellow': '\033[33m',
    'limpa': '\033[m'
}
print('-='*15)
print('{}{}Conversor de bases numéricas{}'.format(text['yellow'],
                                                  text['bold'],
                                                text['limpa']))
print('-='*15)

num = int(input('Número inteiro: '))
print('\nVocê digitou {}{}{}.\n\nEscolha\n\n[1] para converter para {}BINÁRIO{}\n[2] para converter para {}OCTAL{}\n[3] para converter para {}HEXADECIMAL{}'.format(
    text['bold'],
    num,
    text['limpa'],
    text['bold'],
    text['limpa'],
    text['bold'],
    text['limpa'],
    text['bold'],
    text['limpa']
    ))

choice = int(input('\nSua escolha: '))

if choice == 1:
    print('{} convertido para binário vale {}'.format(
        num,
        bin(num)
    ))

elif choice == 2:
    print('{} convertido para octal vale {}'.format(
        num,
        oct(num)
    ))

elif choice == 3:
    print('{} convertido para hexadecimal vale {}'.format(
        num,
        hex(num)
    ))

else:
    print('Opção inválida!\nTente novamente.')
