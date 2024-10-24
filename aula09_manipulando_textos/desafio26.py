
'''
Faça um programa que leia uma frase pelo teclado e mostre:
1. Quantas vezes aparece a letra "a";
2. Em que posição ela aparece a primeira vez;
3. Em que posição ela aparece a última vez.
'''

frase = input('Frase: ').strip().upper()
print('Quantas vezes a letra "A" aparece na frase? {}\nEm que posição "A" aparece a primeira vez? {}\nEm que posição "A" aparece a última vez? {}'.format(
    frase.count('A'),
    frase.replace(" ", "").find('A') + 1, # O comando `replace` e o `+1` deixam o código mais compreensível para o usuário final. Isso facilita a leitura do usuário, pois ele não considerará o espaço do meio como uma letra, ao contrário do Python.
    frase.replace(" ", "").rfind('A') + 1
))
