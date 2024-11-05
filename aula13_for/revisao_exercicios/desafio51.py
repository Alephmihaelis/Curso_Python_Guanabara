
# Pede que o usuário informe o primeiro termo da P.A.
p_termo = int(input('Primeiro termo: '))

# Pede que o usuário informe a razão da P. A.
razao = int(input('Razão: '))

# Cálcula o enésimo termo da P.A. Em razão da lógica do Python, acrescenta `+ razao` depois da multiplicação, para que o Python mostre 10 termos, e não 9
enesimo = p_termo + (10-1) * razao + razao

# Pula duas linhas
print('\n\n')

# Mostra o primeiro termo
print('Primeiro termo: {}'.format(p_termo))

# Mostra o segundo termo
print('Razão: {}'.format(razao))

# Mostra os dez primeiros termos
print('Dez primeiros termos da P.A.: ')

# `Loop` que calcula os dez primeiros termos
for num in range(p_termo, enesimo, razao):
    
    # Mostra os termos
    print(num, end=' -- ')

# Informa o fim do programa
print('\nFim dos dez primeiros termos da P.A.!')
