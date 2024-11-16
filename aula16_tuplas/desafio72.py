
print('~' * 20)
print('NÚMERO POR EXTENSO')
print('~' * 20)

num_tuple = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
             'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
             'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
             'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
             'Dezenove', 'Vinte')

while True:

    num = int(input('Digite um número de 0 a 20 para ver-lhe escrito por extenso: '))
    if num >= 0 and num < 20:
        print(f'O número {num}, escrito por extenso é "{num_tuple[num]}".')
        
        response = input('Quer continuar? [S/N] ').upper().strip()[0]
        
        if response == 'N':
            print('Programa encerrado.')
            break
    else:
        print('Opção inválida. Tente novamente.')
        print('=-' * 30)