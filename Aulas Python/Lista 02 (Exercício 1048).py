# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


# Salário	Percentual de Reajuste
# 0 - 400.00         15%
# 400.01 - 800.00    12%
# 800.01 - 1200.00   10%
# 1200.01 - 2000.00  7%
# Acima de 2000.00   4%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho.

salario = float(input())
if salario <= 400.00:
    reajuste = salario * 0.15
    percentual = 15
elif salario <= 800.00:
    reajuste = salario * 0.12
    percentual = 12
elif salario <= 1200.00:
    reajuste = salario * 0.10
    percentual = 10
elif salario <= 2000.00:
    reajuste = salario * 0.07
    percentual = 7
else:
    reajuste = salario * 0.04
    percentual = 4

novo_salario = salario + reajuste

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')

# A variavél salario é responsável por converter o valor inserido em ponto flutuante, podendo agora ter casas decimais
# A condicional if vai impor uma condição, nesse caso se a variável salario for menor ou igual a 400.000
# O reajuste será 15% do valor do salário. Essa variável armazena o valor calculado
# A variável percentual receberá o valor de 15
# Caso o valor da variável salario seja menor ou igual a 800.00, as condições do primeiro elif serão executadas
# O mesmo valerá para os demais elif baseados no valor da variável salario
# A variável novo_salario somará o valor das variáveis salario e reajuste com base nas condições impostas anteriormente