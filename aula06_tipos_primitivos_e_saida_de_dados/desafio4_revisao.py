
something = input('Digite alguma coisa: ')

print('O tipo primitivo de "{}" é {}'.format(something, type(something)))
print('"{}" é alfabético? {}'.format(something, something.isalpha()))
print('"{}" é alfanumérico? {}'.format(something, something.isalnum()))
print('"{}" pode ser um número? {}'.format(something, something.isnumeric()))
print('"{}" é um número? {}'.format(something, something.isdigit()))
print('"{}" está capitalizado? {}'.format(something, something.istitle()))
print('"{}" está de todo em letras maiúsculas? {}'.format(something, something.isupper()))
print('"{}" está de todo em letras minúsculas? {}'.format(something, something.islower()))
print('"{}" pode ser impresso? {}'.format(something, something.isprintable()))
print('"{}" compõe-se só de espaços? {}'.format(something, something.isspace()))

