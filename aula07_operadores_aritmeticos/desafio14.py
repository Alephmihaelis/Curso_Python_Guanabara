
"""
Converte uma temperatura digitada em Celsius para Fahrenheit.
OBS.: Adicionei também o código que faz a conversão de Fahrenheit para Celsius.
"""

MSG = 'CONVERSOR DE TEMPERATURAS'

print('=' * len(MSG))
print(MSG)
print('=' * len(MSG))

print('''Convertemos Celsius em Fahrenheit e vice-versa.
[1] para converter Celsius para Fahrenheit
[2] para converter Fahrenheit para Celsius''')

while True:
    try:
        escolha = int(input())

        if escolha == 1:
            print('Temperatura em ºC:')
            temp_c = float(input())
            print('A temperatura {:.1f}ºC, em Fahrenheit, vale {:.1f}ºF'.format(temp_c, temp_c * 1.8 + 32,))
            break
        elif escolha == 2:
            print('Temperatura em ºF:')
            temp_f = float(input())
            print('A temperatura {:.1f}ºF equivale a {:.1f}ºC'.format(temp_f, (temp_f - 32) / 1.8))
            break
        else:
            print('Insira um número válido.')
            continue

    except ValueError:
        print('Insira um número válido.')
        continue
