

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n
