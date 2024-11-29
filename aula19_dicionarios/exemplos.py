
dados = []
dados2 = list()

dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

dados3 = {
    'nome': 'Pedro',
    'idade': 25
}
print(dados3['nome'])
print(dados3['idade'])

dados3['sexo'] = 'M'
del dados3['idade']
print(dados3)

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')

locadora = [
    {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'},
    {
    'titulo': 'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'        
    },
    {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Machowski'
    }
]

print(locadora[0]['ano'])
print(locadora[2]['titulo'])
