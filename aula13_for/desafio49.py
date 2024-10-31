
# Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço `for`.

num = int(input('Digite um número para ver-lhe a tabuada: '))
for tab in range(1, 11):
    print('{} x {} = {}'.format(num, tab, num * tab))
