
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

object = input('Digite alguma coisa: ')
print('\033[7;36;43mO tipo primitivo de "{}" é {}\033[m'.format(
    object,
    type(object)
    ))

print('\033[1;32;43m"{}" só tem espaços? {}\033[m'.format(
    object,
    object.isspace()
    ))

print('\033[4;33;44m"{}" pode ser um número? {}\033[m'.format(
    object,
    object.isnumeric()
    ))

print('\033[1;34;45m"{}" é alfabético? {}\033[m'.format(
    object,
    object.isalpha()
    ))

print('\033[32;47m"{}" é alfanumérico? {}\033[m'.format(
    object,
    object.isalnum()
    ))

print('\033[36;46m"{}" só tem letras maiúsculas? {}\033[m'.format(
    object,
    object.isupper()
    ))

print('\033[1;31;41m"{}" só tem letras minúsculas? {}\033[m'.format(
    object,
    object.islower()
    ))

print('\033[4;32;43m"{}" está capitalizado? {}\033[m'.format(
    object,
    object.istitle()
    ))

print('\033[1;33;44mEm "{}", todos os caracteres são ASCII? {}\033[m'.format(
    object,
    object.isascii()
    ))

print('\033[7;31;45mEm "{}", todos os caracteres são decimais? {}\033[m'.format(
    object,
    object.isdecimal()
    ))

print('\033[1;34;44m"{}" é um identificador válido? {}\033[m'.format(
    object,
    object.isidentifier()
    ))
