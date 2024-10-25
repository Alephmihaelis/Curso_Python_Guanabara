
something = input('Digite alguma coisa: ')

print('\033[4mO tipo primitivo de "{}" é {}\033[m'.format(
    something,
    type(something)
    ))

print('\033[1m"{}" é alfabético? {}\033[m'.format(
    something,
    something.isalpha()
    ))

print('\033[0;37;47m"{}" é alfanumérico? {}\033[m'.format(
    something,
    something.isalnum()
    ))

print('\033[7;36;36m"{}" pode ser um número? {}\033[m'.format(
    something,
    something.isnumeric()
    ))

print('\033[1;35;45m"{}" é um número? {}\033[m'.format(
    something,
    something.isdigit()
    ))

print('\033[1;34;44m"{}" está capitalizado? {}\033[m'.format(
    something,
    something.istitle()
    ))

print('\033[4;33;43m"{}" está de todo em letras maiúsculas? {}\033[m'.format(
    something,
    something.isupper()
    ))

print('\033[1;32;42m"{}" está de todo em letras minúsculas? {}\033[m'.format(
    something,
    something.islower()
    ))

print('"{}" pode ser impresso? {}'.format(
    something,
    something.isprintable()
    ))

print('"{}" compõe-se só de espaços? {}'.format(
    something,
    something.isspace()
    ))
