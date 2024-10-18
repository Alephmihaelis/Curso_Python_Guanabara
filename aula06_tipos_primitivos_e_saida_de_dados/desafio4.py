# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

object = input('Digite alguma coisa: ')
print('O tipo primitivo de "{}" é {}'.format(object, type(object)))
print('"{}" só tem espaços? {}'.format(object, object.isspace()))
print('"{}" é um número? {}'.format(object, object.isnumeric()))
print('"{}" é alfabético? {}'.format(object, object.isalpha()))
print('"{}" é alfanumérico? {}'.format(object, object.isalnum()))
print('"{}" só tem letras maiúsculas? {}'.format(object, object.isupper()))
print('"{}" só tem letras minúsculas? {}'.format(object, object.islower()))
print('"{}" está capitalizado? {}'.format(object, object.istitle()))
print('Em "{}", todos os caracteres são ASCII? {}'.format(object, object.isascii()))
print('Em "{}", todos os caracteres são decimais? {}'.format(object, object.isdecimal()))
print('"{}" é um identificador válido? {}'.format(object, object.isidentifier()))
