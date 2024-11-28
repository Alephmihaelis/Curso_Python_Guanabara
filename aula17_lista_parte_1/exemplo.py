
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim') # Isto é uma `TUPLA`.
print(lanche[2])
'''
lanche[3] = 'picolé' :: Este código retorna um erro, porque as tuplas são imutáveis: não é possível mudar o conteúdo delas.
'''

tuple() # Tupla: usa ()
list() # Lista: usa []

lanche2 = ['hambúrguer', 'suco', 'pizza', 'pudim']
lanche2[3] = 'picolé'
print(lanche2)

lanche2.append('biscoito') # Simplesmente adiciona um item à lista
print(lanche2)

lanche2.insert(0, 'torta') # Adiciona um item à lista numa posição específica
print(lanche2)

del lanche2[0] # ou lanche2.pop(0) :: Ordinariamente, o método `pop` é usado para eliminar o último item da lista: basta digitar lanche2.pop()

# lanche2.remove('torta') # Elimina o elemento pelo seu conteúdo, em vez do índice
print(lanche2)

if 'pizza' in lanche2:
    lanche2.remove('pizza')

valores = list(range(4,11))
print(valores)

valores2 = [8, 2, 5, 4, 9, 3, 0]
print(valores2)
valores2.sort() # Ordena os valores
print(valores2)
valores2.sort(reverse=True) # Põe na ordem inversa
print(valores2)
print(len(valores2))
