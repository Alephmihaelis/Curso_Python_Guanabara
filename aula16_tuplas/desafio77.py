
palavras = ('joao', 'melancia', 'madeira',
            'bobo', 'computador', 'python')

for p in palavras:
    print(f'\nNa palavra «{p.upper()}», as vogais são: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
