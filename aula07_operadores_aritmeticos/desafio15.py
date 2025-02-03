
"""
Programa que pergunta a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Depois, calcula o preço a ser pago, sabendo que o carro custa R$60 por dia
e R$0.15 por km rodado.
"""

while True:
    try:
        print('Quilômetros rodados.')
        km_rodados = float(input())

        print('Dias alugados.')
        dias_alugados = int(input())
        print('''O carro rodou {:.2f}km.
O carro foi alugado por {} dias.
Preço total: R${:.2f}'''.format(km_rodados, dias_alugados,
dias_alugados * 60 + 0.15 * km_rodados,))
        break
    except ValueError:
        print('Insira um valor válido.')
        continue
    except Exception as e:
        print(f'Erro {e}. Tente novamente')
        continue
