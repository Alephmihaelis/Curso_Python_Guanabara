
"""
Programa que lê um número inteiro e mostra na tela seu sucessor e antecessor.
"""
import sys

TENTATIVAS = 0

MSG = 'ANTECESSOR E SUCESSOR'
print('=' * len(MSG))
print(MSG)
print('=' * len(MSG))

print('Digite um número inteiro.')

while True:
    try:
        num = int(input())
        print(f"""Antecessor de \033[1m"{num}\033[m": \033[1m"{num-1}"\033[m.
Sucessor de \033[1m"{num}"\033[m: \033[1m"{num+1}"\033[m.""")
        break
    except ValueError:
        TENTATIVAS += 1
        if TENTATIVAS == 3:
            print('Número máximo de tentativas atingido. PROGRAMA ENCERRADO.')
            sys.exit()
        print('Digite um valor válido.')
        continue
    except Exception as e:
        TENTATIVAS += 1
        if TENTATIVAS == 3:
            print('Número máximo de tentivas atingido.\nPROGRAMA ENCERRADO.')
            sys.exit()
        print(f'Ocorreu um erro inesperado: {e}')
        continue
print('=' * 25)
