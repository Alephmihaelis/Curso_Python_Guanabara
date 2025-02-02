
"""
Programa que lê duas notas de um aluno, calcula e mostra sua média.
"""

print('Digite a primeira nota.')
notaUm = float(input())

print('Digite a segunda nota.')
notaDois = float(input())

print(f"""As notas do aluno são {notaUm} e {notaDois}.
A média do aluno é {(notaUm + notaDois) / 2:.1f}""")
