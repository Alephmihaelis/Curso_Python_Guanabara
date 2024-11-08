
# Solicita ao usuário que digite uma frase: `input`
# Remove espaços no início e no fim: `strip`
# Converte tudo para maiúsculas: `upper`    
phrase = input('Digite uma frase: ').strip().upper()

# Separa a frase em palavras: `split`
words = phrase.split()

# Junta todas as palavras  em uma única string, sem espaços entre elas: `join`
all = ''.join(words)

# Cria uma variável vazia para armazenar a frase invertido
reverse = ''

# Laço de repetição para percorrer `all` de trás para frente
# `range(len(all)-1, -1, -1)` começa do último índice da string e vai até o índice 0

for letter in range(len(all)-1, -1, -1):
    # Concatena cada letra a 'inverso', criando a string invertida
    reverse += all[letter]

# Verifica se `reverse` é igual à string original sem espaços
if reverse == all:
    # Se for igual, significa que a string é um palíndromo
    print('Há um palíndromo!')
else:
    # Caso contrário, a frase não é um palíndromo
    print('A frase digitada não é um palíndromo. :(')
