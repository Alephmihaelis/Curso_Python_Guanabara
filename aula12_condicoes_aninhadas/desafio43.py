
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela: 1. Abaixo de 18.5: Abaixo do peso; 2. Entre 18.5 e 25: Peso ideal; 25 até 30: Sobrepreso; 30 até 40: Obesidade; Acima de 40: Obesidade mórbida

peso = float(input('Peso (em kg): '))
altura = float(input('Altura (em m): '))
imc = peso / (altura ** 2)

print('O IMC vale {:.1f}'.format(imc))

if imc < 18.5:
    print('CLASSIFICAÇÃO: Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('CLASSIFICAÇÃO: Peso ideal')
elif imc >= 25 and imc <= 30:
    print('CLASSIFICAÇÃO: Sobrepreso')
elif imc >= 30 and imc <= 40:
    print('CLASSIFICAÇÃO: Obesidade')
else:
    print('CLASSIFICAÇÃO: Obesidade mórbida')
