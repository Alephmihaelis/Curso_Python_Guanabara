
# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa perguntará `o valor da casa`, `o salário do comprador` e `em quantos anos ele pagará`. Calcule o valor da prestação mensal, sabendo que ela `não pode exceder 30% do salário`, ou então o empréstimo será negado.

import emoji

format_text = {
    'red': '\033[31m',
    'yellow': '\033[33m',
    'green': '\033[32m',
    'bold': '\033[1m',
    'limpa': '\033[m'
}

print('=-'*10)
print('{}Empréstimo bancário!{}'.format(
    format_text['bold'],
    format_text['limpa']
))
print('=-'*10)

price = float(input('{}Valor da casa: R${}'.format(format_text['green'],
                                                   format_text['limpa']
                                                   )))

salary = float(input('{}Salário do comprador: R${}'.format(format_text['green'],
                                                       format_text['limpa']
                                                       )))

years = int(input('{}Anos de financiamento: {} '.format(format_text['red'],
                                                        format_text['limpa']
                                                        )))

prestacao = price / (years * 12)

limit = salary * (30/100)

if prestacao <= limit:
    print('Parabéns!\nSeu empréstimo foi {}APROVADO!{} {}\nCada prestação custará {}R${:.2f}{}.'.format(
    format_text['green'],
    format_text['limpa'],
    emoji.emojize(':grinning_face:'),
    format_text['green'],
    prestacao,
    format_text['limpa']
    ))

else:
    print('Que pena!\nSeu empréstimo foi {}NEGADO{} {}, pois cada prestação custaria {}R${:.2f}{}.'.format(
        format_text['red'],
        format_text['limpa'],
        emoji.emojize(':sad_but_relieved_face:'),
        format_text['red'],
        prestacao,
        format_text['limpa']
    ))
