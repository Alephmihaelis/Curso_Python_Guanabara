
'''
Erros e exceções.
'''

#primt(x) # Erro de sintaxe.

# O erro sintático é só um tipo de erro. HÁ OUTROS ERROS.

#print(x) # Não há erro sintático, mas há erro, porque a variável `x` não foi inicializada. Isso é um ERRO SEMÂNTICO. Neste caso, o `x` retorna uma EXCEÇÃO `NameError`

'''
EXEMPLOS DE TIPOS DE EXCEÇÕES:

NameError
ValueError
ZeroDivisionError
TypeError
IndexError
KeyError
'''

try:
    pass

except:
    pass

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir por zero.')

except KeyboardInterrupt:
    print('O usuário escolheu não inserir o dado.')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre. :D')