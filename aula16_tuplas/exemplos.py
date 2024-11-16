
# Variáveis compostas: "tuplas", "listas", "dicionários"

lanche = ('hambúrger', 'suco', 'pizza', 'doce')
# Tuplas são imutáveis.

print(lanche[2]) # Retorna 'pizza'
print(lanche[0:2]) # Retorna 'hambúrguer', 'suco'
print(lanche[1:]) # Retorna 'suco', 'pizza', 'doce'
print(lanche[-1]) # Retorna 'doce'
print(len(lanche)) # Retorna '4'

for comida in lanche: # Atribui uma variável de `lanche` a cada iteração de `comida`
    print(comida)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8)) # Mostra o índice em que 8 está.

pessoa = ('Gustavo', 25, 'Masculino', 99.88)
del(pessoa) # `del` apaga a variável `pessoa`
