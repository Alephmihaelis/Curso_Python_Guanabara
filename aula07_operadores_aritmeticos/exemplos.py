
"""
Exemplos
"""

MSG = 'EXEMPLOS DE ORDEM DE PRECEDÊNCIA DOS OPERADORES ARITMÉTICOS'

print('=' * len(MSG))
print(MSG)
print('=' * len(MSG))

exemploUm = 5+3*2
print(exemploUm)
print(f'''«5+3*2» retorna {exemploUm} em razão da ordem de precedência dos operadores.
O operador * tem prioridade sobre o operador +, e, por isso, 3*2 é realizado primeiro;
depois, 5 + o resultado de 3*2.''')
print('='*30)

exemploDois = 3*5+4**2
print(exemploDois)
print('''«3*5+4**2» retorna 31 em razão da ordem de precedência dos operadores.
O operador ** tem prioridade sobre os demais operadores da conta.
Primeiro faz-se 4**2,depois, 3*5, e depois, soma-se tudo.''')
print('='*30)

exemploTres = 3*(5+4)**2
print(exemploTres)
print('''«3*(5+4)**2» retorna 243. Os parênteses () têm prioridade sobre qualquer
outro operador. Então, primeiro faz-se 5+4,depois, eleva-se o resultado de 5+4 ao
quadrado, depois, multiplica-se por 3 esse mesmo resultado.''')
print('=' * 30)

exemploQuatro = 5+3*2 # Primeiro 3*2; depois o resto.

exemploCinco = 5**2 # É o mesmo que 5²

exemploSeis = 5**3 # É o mesmo que 5³.

exemploSete = 19//2 # Retorna a divisão inteira de 19//2. Nesse caso, 9, e não 9.5

exemploOito = 19/2 # Retorna a divisão de 19/2, por um número flutuante. Nesse caso, 9.5

exemploNove = 356**522 # É mesmo que 356⁵²²

exemploDez = 18%2 # Retorna o resto da divisão de 18/2. Neste caso, retorna 0.

exemploOnze = 122%3 # Retorna o resto da divisão de 122/3. Neste caso, 2.

exemploDoze = 4**3 # É o mesmo que 4³

pow(4,3) # Função interna do Python usada para calcular exponenciação. É o mesmo que 4**3.

exemploTreze = 81**(1/2) # Método utilizado para calcular a raiz quadrada de um número: eleva-se esse número a meio.
# Importante: o meio deve estar entre parênteses, para ser calculado primeiro.

exemploQuatorze = 25**(1/2) # Calcula a raiz quadrada de 25.

exemploQuinze = 127**(1/3) # Calcula a raiz cúbica de 127.

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

'''
Formatação de código: Se o resultado que tenho precisa ser exibido uma vez só,
não preciso (e não devo) armazená-lo em uma variável. Basta que passe seus
parâmetros uma só vez, como na função format acima.
'''
