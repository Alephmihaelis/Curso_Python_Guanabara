
times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo',
             'Internacional', 'São Paulo', 'Cruzeiro', 'Bahia',
             'Vasco', 'Atlético-MG', 'Corinthians', 'Grêmio',
             'Vitória', 'Fluminense', 'Criciúma', 'Juventude',
             'Bragantino', 'Athletico-PR', 'Cuiabá', 'Atlético-GO')

print('~' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('~' * 30)

print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('~' * 30)

print(f'Os últimos 4 colocados são: {times[-4:]}')
print('~' * 30)

print(f'Times em ordem alfabética: {sorted(times)}')
print('~' * 30)

print(f'O Bahia está na {times.index("Bahia") + 1}ª posição.')