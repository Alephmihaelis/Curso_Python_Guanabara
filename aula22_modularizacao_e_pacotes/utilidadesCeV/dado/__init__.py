
def leiaDinheiro(msg):
    valid = False
    while not valid:
        valor = input(msg).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print('\033[31mERRO! Valor inválido.\033[m')
        else:
            valid = True
            return f'Valor informado: {valor}'
