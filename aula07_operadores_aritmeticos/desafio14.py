
# Converta uma temperatura digitada em Celsius para Fahrenheit.
# OBS.: Adicionei também o código que faz a conversão de Fahrenheit para Celsius.

colors = {
    'red_bg': '\033[41m',
    'blue_bg': '\033[44m',
    'bold': '\033[1m',
    'limpa': '\033[m'
}

print('Temperatura de Celsius para Fahrenheit')
temp_c = float(input('Temperatura em ºC: '))
print('{}A temperatura {:.1f}ºC, em Fahrenheit, vale {:.1f}ºF{}'.format(
    colors['red_bg'],
    temp_c, temp_c * 1.8 + 32,
    colors['limpa']
    ))

print('-'*40)

print('Temperatura de Fahrenheit para Celsius')
temp_f = float(input('Temperatura em ºF: '))
print('{}A temperatura {:.1f}ºF equivale a {:.1f}ºC{}'.format(
    colors['blue_bg'],
    temp_f,
    (temp_f - 32) / 1.8,
    colors['limpa']
    ))
