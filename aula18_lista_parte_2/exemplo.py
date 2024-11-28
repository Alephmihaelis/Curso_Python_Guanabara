
dados = []

dados.append('Pedro')
dados.append(25)
print(dados[0]) # `Pedro`
print(dados[1]) # `25`

pessoas = []

pessoas.append(dados[:])

pessoas = [
    ['Pedro', 25],
    ['Maria', 19],
    ['João', 32]
]

print(pessoas[0][0]) # Acessa o item `0` de `pessoas`, e retorna `Pedro`
print(pessoas[1][1]) # Acessa o item `1` de `pessoas`, e retorna 19
print(pessoas[2][0]) # Acessa o item `2` de `pessoas`, e retorna `João`
print(pessoas[1]) # Retorna todo o item `1` de pessoas

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [
    ['João', 19],
    ['Ana', 33],
    ['Joaquim', 13],
    ['Maria', 45]
]

galera = []
dado = []

for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

totmai = 0
totmen = 0

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Há {totmai} maiores e {totmen} menores de idade.')