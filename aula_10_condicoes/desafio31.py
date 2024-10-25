
'''
Faça um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem do ônibus, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.
'''

distance = float(input('Distância da viagem: '))

if distance <= 200:
    print('A passagem de uma viagem de {:.1f}km custa R${:.2f}'.format(
        distance,
        0.50 * distance
    ))
else:
    print('A passagem de uma viagem de mais de 200km custa R${:.2f}'.format(
        0.45 * distance
    ))
