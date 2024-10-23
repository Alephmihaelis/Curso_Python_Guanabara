
'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1. O nome com todas as letras maiúsculas;
2. O nome com todas as letra minúsculas;
3. Quantas letras ao todo (sem considerar espaços);
4. Quantas letras tem o primeiro nome.
'''

full_name = input('Nome completo:')

print('Nome com todas as letras maiúsculas: {}\nNome com todas as letras minúsculas: {}\nLetras ao todo, sem considerar espaços: {}'.format(
    full_name.upper(),
    full_name.lower(),
    len(full_name.replace(" ", ""))
    ))

# Por alguma razão, este código NÃO ESTÁ FUNCIONANDO. Já testei tudo. A lógica me parece correta, e também a sintaxe. Não sei qual possa ser o erro.
