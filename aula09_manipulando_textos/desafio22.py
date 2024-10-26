
# O método `strip` remove os espaços inúteis à esquerda e à direita do resultado do `input`.

name = input('Nome completo: ').strip()
print('O nome digitado é: {}\nMAIÚSCULAS: {}\nMINÚSCULAS: {}\nTOTAL DE LETRAS (SEM ESPAÇOS): {}\nTOTAL DE LETRAS DO PRIMEIRO NOME: {}'.format(
    name,
    name.upper(),
    name.lower(),
    len(name.replace(" ","")),
    # Aqui começam minhas dúvidas: pois o Python me retorna 9, se digito "Paulo Bobo". Mas "Paulo Bobo", sem os espaços, possui somente 8 caracteres. Quando faço o teste de mesa e imprimo `print(len(name.replace(" ", "")))`, o Python me retorna `PauloBobo`; sendo assim, a função `len` deveria me retornar 8, e não 9. Não sei qual o problema.
    len(name.split()[0]) # Aqui há outro problema. Ele me retorna "Paulo", e isto está correto; mas a função `len` me retorna 5, e não 4 (que é o resultado esperado).
))

# OBS.: O que me confunde é que o resultado que me é mostrado é o mesmo que o resultado da resolução do professor, quando digito seus exemplos.

# Código do professor:

nome = str(input('Digite seu nome completo: ')).strip() # This `str` is redundant because all `input` is `str` by default.
print('Analisando seu nome...')
print('Seu nome em maiúsculas é "{}"'.format(
    nome.upper()
    ))

print('Seu nome em minúsculas é "{}"'.format(
    nome.lower()
    ))

print('Seu nome tem ao todo "{}" letras'.format(
    len(nome) - nome.count(" ")
    ))

print('Seu primeiro nome tem "{}" letras'.format(
    nome.find(" ")
    ))
