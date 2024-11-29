
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

# Tupla: pessoas = ()
# Lista: pessoas = []
# Dicionários: pessoas = {}

pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

state = dict()
brazil = []

for c in range(0, 3):
    state['uf'] = input('Unidade Federativa: ')
    state['sigla'] = input('Sigla do Estado: ')
    brazil.append(state.copy())

for state in brazil:
    for k, v in state.items():
        print(f'O campo {k} tem valor {v}')
