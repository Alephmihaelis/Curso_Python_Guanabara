
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

km_p = float(input('Quilômetros rodados: '))
dias = int(input('Por quantos dias o carro foi alugado? '))
print('O carro rodou {:.2f}km.\nO carro foi alugado por {} dias.\nPreço total: R${:.2f}'.format(km_p, dias, dias * 60 + 0.15 * km_p))
