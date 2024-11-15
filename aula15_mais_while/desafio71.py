
valor = int(input('Valor a sacar: R$'))

# A variável `total` é inicializada com o valor de `valor`.
total = valor

# `cedula` é inicializada com o valor 50, indicando que o processo de saque começa com cédulas de 50 reais.
cedula = 50

# `tot_ced` serve para contar o número de cédulas de cada valor.
tot_ced = 0

while True:
    # Verifica se `total` é maior ou igual ao valor da cédula atual.
    if total >= cedula:
        # Caso a condição anterior seja verdadeira, o valor da cédula é subtraído do total, reduzindo o valor a ser sacado.
        total -= cedula
        # Ao retirar uma cédula, a variável `tot_ced` é incrementada em 1, contando quantas cédulas do valor atual foram retiradas.
        tot_ced += 1
    # Caso `total` seja menor que o valor da cédula atual, entra na parte do código que mostra a quantidade de cédulas retiradas e de mudar para o próximo valor de cédula.
    else:
        # Verifica se alguma cédula foi retirada (tot_ced > 0). Se sim, mostra a quantidade de cédulas retiradas até o momento.
        if tot_ced > 0:
            # Mostra a quantidade de cédulas retiradas e o valor delas.
            print(f'Total de {tot_ced} células de R${cedula:.2f}')
        # Se o valor da cédula atual for 50, o código muda o valor da cédula para 20 reais, passando a tentar sacar com cédulas de 20 reais na próxima iteração.
        if cedula == 50:
            cedula = 20
        # Se a cédula atual for de 20 reais, ela será substituída por cédulas de 10 reais.
        elif cedula == 20:
            cedula = 10
        # Se a cédula atual for de 10 reais, o próximo valor de cédula será 1 real.
        elif cedula == 10:
            cedula = 1
        # Após mostrar a quantidade de cédulas retiradas e trocar o valor da cédula, a variável `tot_ced` é reiniciada para zero, porque estamos começando a contar as cédulas de outro valor.
        tot_ced = 0
        # Verifica se o total é zero, i. e., se todo o valor foi sacado. Se sim, `while` é interrompido com break.
        if total == 0:
            break
