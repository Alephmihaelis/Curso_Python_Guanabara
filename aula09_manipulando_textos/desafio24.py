
"""
Programa que lê o nome de uma cidade
e diz se ele começa ou não com a palavra «Santo»
"""

"""
print('Qual o nome da cidade?')
nomeCidade = input().strip().title()
print('''A cidade digitada foi "{}".
Ela começa com "Santo"? {}'''.format(nomeCidade, 'Santo' in nomeCidade.split()[0]))
"""

# Resolvendo o problema com `regex`

import re

def validaNomeCidade(cidade):
    cidadeRegex = re.compile(r'^santo', re.IGNORECASE)
    mo = cidadeRegex.search(cidade)
    if mo:
        print('A cidade digitada começa com «Santo»')
    else:
        print('Essa cidade não começa com «Santo»')

print('Informe o nome da cidade.')
nomeCidade = input()
validaNomeCidade(nomeCidade)
