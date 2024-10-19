
# Converta uma temperatura digitada em Celsius para Fahrenheit.
# OBS.: Adicionei também o código que faz a conversão de Fahrenheit para Celsius.

print('Temperatura de Celsius para Fahrenheit')
temp_celsius = float(input('Temperatura em ºC: '))
print('A temperatura {:.1f}ºC, em Fahrenheit, vale {:.1f}ºF'.format(temp_celsius, temp_celsius * 1.8 + 32))

print('-'*20)

print('Temperatura de Fahrenheit para Celsius')
temp_fahrenheit = float(input('Temperatura em ºF: '))
print('A temperatura {:.1f}ºF equivale a {:.1f}ºC'.format(temp_fahrenheit, (temp_fahrenheit - 32) / 1.8))
