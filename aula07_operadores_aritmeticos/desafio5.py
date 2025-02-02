
"""
Programa que lê um número inteiro e mostra na tela seu sucessor e antecessor.
"""
import sys

def encerraPrograma(contador):
    """
    Função que encerra o programa caso o número de tentativas seja igual a 3.
    """
    if contador == 3:
        print('Número máximo de tentativas atingido. Programa encerrado.')
        sys.exit()

cont = 0

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
        cont += 1
        print('Digite um valor válido.')
        encerraPrograma(cont)
        continue
    except Exception as e:
        cont += 1
        print(f'Ocorreu um erro inesperado: {e}')
        encerraPrograma(cont)
        continue
print('=' * 25)
