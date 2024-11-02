
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Não entendi o uso do `for` neste exercício; consegui resolvê-lo com fatiamento, mas não com `for`.

# Revisão.

# Código do professor:

# Solicita ao usuário que digite uma frase, remove espaços do início e do fim,
# e converte toda a frase para letras maiúsculas.
frase = str(input('Digite uma frase: ')).strip().upper()

# Divide a frase em palavras, criando uma lista de palavras separadas por espaços.
palavras = frase.split()

# Junta todas as palavras da lista em uma única string, removendo os espaços.
junto = ''.join(palavras)

# Inicializa uma string vazia para armazenar a versão invertida da string 'junto'.
inverso = ''

# Loop que percorre a string 'junto' de trás para frente.
for letra in range(len(junto)-1, -1, -1):
    # Adiciona cada letra da string 'junto' à string 'inverso'.
    inverso += junto[letra]

# Compara a string original 'junto' com a string invertida 'inverso'.
if inverso == junto:
    # Se forem iguais, imprime que a frase é um palíndromo.
    print('A frase digitada é um palíndromo!')
else:
    # Se não forem iguais, imprime que a frase não é um palíndromo.
    print('A frase digitada não é um palíndromo!')
