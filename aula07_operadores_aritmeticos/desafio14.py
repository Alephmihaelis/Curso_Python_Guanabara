
# Converta uma temperatura digitada em Celsius para Fahrenheit.
# OBS.: Adicionei também o código que faz a conversão de Fahrenheit para Celsius.

print('Temperatura de Celsius para Fahrenheit')
temp_c = float(input('Temperatura em ºC: '))
print('A temperatura {:.1f}ºC, em Fahrenheit, vale {:.1f}ºF'.format(temp_c, temp_c * 1.8 + 32))

print('-'*40)

print('Temperatura de Fahrenheit para Celsius')
temp_f = float(input('Temperatura em ºF: '))
print('A temperatura {:.1f}ºF equivale a {:.1f}ºC'.format(temp_f, (temp_f - 32) / 1.8))
