
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salário do funcionário: R$'))

print('Com 15% de aumento, o salário do funcionário, que é de R${:.2f}, passará a ser \nR${:.2f}'.format(salario, salario + (salario * 15/100)))

# Continuo evitando o uso desnecessário de variáveis, uma vez que o resultado é exibido uma vez só.
