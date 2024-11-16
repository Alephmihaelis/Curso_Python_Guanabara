
print('~' * 20)
print('NÚMERO POR EXTENSO')
print('~' * 20)

num_tuple = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
             'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
             'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
             'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


num = int(input('Digite um número de 0 a 20 para ver-lhe escrito por extenso: '))

while True:
    if num > 20:
        print('Opção inválida. Tente novamente.')
        print('=' * 30)
        num = int(input('Digite um número de 0 a 20 para ver-lhe escrito por extenso: '))
    else:
        break
print('=' * 30)
print(f'O número {num}, escrito por extenso é "{num_tuple[num]}".')
print('=' * 30)