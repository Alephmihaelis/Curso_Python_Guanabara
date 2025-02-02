
"""
Cria um algoritmo que lê um número e mostra seu dobro, triplo e raiz quadrada.
"""
import sys

def encerraPrograma(contador):
    """
    Função que encerra o programa caso o número de tentativas seja igual a 3.
    Recebe o contador como parâmetro.
    """
    if contador == 3:
        print('Número máximo de tentativas atingido. Programa encerrado.')
        sys.exit()

cont = 0

print('Digite um número.')

while True:
    try:
        num = int(input())
        print(f"""\033[1;33;45mVocê digitou "{num}".
O dobro de "{num}" vale {num * 2}.
O triplo de "{num}" é {num * 3}.
A raiz quadrada de "{num}" vale {num ** (1/2)}.\033[m""")
        break

    except ValueError:
        cont += 1
        print('Por favor, insira um número válido.')
        encerraPrograma(cont)
    except Exception as e:
        cont += 1
        print(f'{e}. Tente novamente.')
        encerraPrograma(cont)
