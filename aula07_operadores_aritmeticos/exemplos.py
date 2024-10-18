
# Exemplos

alfa = 5+3*2
print(alfa)

print('"alfa" retorna 11 em razão da ordem de precedência dos operadores. \nO operador * tem prioridade sobre o operador +, e, por isso, 3*2 é realizado primeiro;\ndepois, 5 + o resultado de 3*2.')

print('='*30)

beta = 3*5+4**2
print(beta)

print('"beta" retorna 31 em razão da ordem de precedência dos operadores. O operador ** tem prioridade\nsobre os demais operadores da conta.\nPrimeiro faz-se 4**2,\ndepois, 3*5,\ne depois, soma-se tudo.')

print('='*30)


gama = 3*(5+4)**2

print('"gama" retorna 243. Os parênteses () têm prioridade sobre qualquer outro operador. \nEntão, primeiro faz-se 5+4,\ndepois, eleva-se o resultado de 5+4 ao quadrado,\ndepois, multiplica-se por 3\nesse mesmo resultado.')

delta = 5+3*2
# Primeiro 3*2.

epsilon = 5**2
# É o mesmo que 5²

zeta = 5**3
# É o mesmo que 5³.

eta = 19//2
# Retorna a divisão inteira de 19//2, isto é, retorna um número inteiro. Nesse caso, 9 (e não 9.5)

teta = 19/2
# Retorna a divisão de 19/2, por um número flutuante. Nesse caso, 9.5

iota = 356**522
# É mesmo que 356⁵²²

kappa = 18%2
# Retorna o resto da divisão de 18/2. Neste caso, retorna 0.

lammbda = 122%3
# Retorna o resto da divisão de 122/3. Neste caso, 2.

mi = 4**3
# É o mesmo que 4³

pow(4,3)
# Função interna do Python usada para calcular exponenciação. É o mesmo que 4**3.

ni = 81**(1/2)
# Método utilizado para calcular a raiz quadrada de um número: eleva-se esse número a meio.
# Importante: o meio deve estar entre parênteses, para ser calculado primeiro.

csi = 25**(1/2)
# Calcula a raiz quadrada de 25.

omicron = 127**(1/3)
# Calcula a raiz cúbica de 127.

# print('Oi' + 'Olá')
# Concatena 'Oi' e 'Olá': resulta 'OiOlá'

#print('Oi'*5)
# Imprime a string 'Oi' cinco vezes.

# print('='*20)
# Imprime a string '=' vinte vezes.

name = input('Qual é seu nome? ')
print('Prazer em te conhecer, {:=^20}!'.format(name))

# O código entre colchetes é para alinhamento.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}'.format(n1+n2))

# Formatação de código: Se o resultado que tenho precisa ser exibido uma vez só, não preciso (e não devo) armazená-lo em uma variável. Basta que passe seus parâmetros uma só vez, como na função format acima.