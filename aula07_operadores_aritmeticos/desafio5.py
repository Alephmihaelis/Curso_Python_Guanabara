
"""
Programa que lê um número inteiro e mostra na tela seu sucessor e antecessor.
"""
from sys import exit

tentativas = 0

MSG = 'ANTECESSOR E SUCESSOR'
print('=' * len(MSG))
print(MSG)
print('=' * len(MSG))

print('Digite um número inteiro.')

while True:
    try:
        num = int(input())
        print("""Antecessor de \033[1m"{}\033[m": \033[1m"{}"\033[m.
Sucessor de \033[1m"{}"\033[m: \033[1m"{}"\033[m.""".format(
num, (num - 1), num, (num + 1)))
        break
    except ValueError:
        tentativas += 1
        if tentativas == 3:
            print('Número máximo de tentativas atingido. PROGRAMA ENCERRADO.')
            exit()
        print('Digite um valor válido.')
        continue
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
        continue
print('=' * 25)