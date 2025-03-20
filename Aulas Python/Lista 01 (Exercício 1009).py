# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

# Entrada
# O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.

# Saída
# Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

nome = input()
salario = float(input())
vendas = float(input())

total = (vendas * 15) / 100 + salario

print(f'TOTAL = R$ {total:.2f}')

# nome é uma variavél onde o primeiro nome do vendedor deverá ser inserido
# salario = é um valor flutuante que será inserido pelo usuário para informar o salário fixo do vendedor
# vendas = é um valor flutuante que será inserido para determinar o número de vendas que ele efetuou por mês
# total = é uma variável que irá calcular o total de vendas realizadas por ele no mês, com um adicional de 15% de comissão e dividindo por 100 para gerar o valor em reais.