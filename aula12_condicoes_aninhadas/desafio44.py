
# Calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento: 1. à vista dinheiro/cheque: 10% de desconto; à vista no cartão: 5% de desconto; em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros

preco = int(input('Valor do produto: R$'))
print('''
Selecione o modo de pagamento:\n
[1] À VISTA EM DINHEIRO E/OU CHEQUE: 10% de desconto
[2] À VISTA NO CARTÃO: 5% de desconto
[3] ATÉ 2x NO CARTÃO: Preço normal
[4] 3x OU MAIS NO CARTÃO: 20% de juros\n''')


escolha = int(input('Forma de pagamento: '))

if escolha == 1:
    desconto = preco * (10/100)
    print('O produto de R${:.2f} custará, com 10% de desconto, R${:.2f}'.format(preco,
                                                                            preco - desconto))
elif escolha == 2:
    desconto = preco * (5/100)
    print('O produto de R${:.2f} custará, com 5% de desconto, R${:.2f}'.format(preco,
                                                                               preco - desconto))
elif escolha == 3:
    parcelas = preco / 2
    print('Se o pagamento for feito em até 2x no cartão, não há descontos nem acréscimos.\nO preço continua R${:.2f}.\nCada parcela custará R${:.2f}'.format(preco,
                                                            parcelas))

elif escolha == 4:
    juros = preco * (20/100)
    preco_final = preco + juros
    parcelas = int(input('Quantas vezes no cartão? '))
    valor_parcelas = preco_final / parcelas
    print('Sua compra será parcelada em {} vezes com juros.\nO produto de R${:.2f} custará, com 20% de juros, R${:.2f}\nCada parcela custará R${:.2f}'.format(
        parcelas,
        preco,
        preco_final,
        valor_parcelas))
else:
    print('Opção inválida.\nSua compra não foi finalizada.')
