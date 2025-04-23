# Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
# S = 1 + 1/2 + 1/3 + … + 1/100

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# A saída contém um valor correspondente ao valor de S.
# O valor deve ser impresso com dois dígitos após o ponto decimal.

S = 0

for i in range(1, 101):
    S += 1 / i

print(f'{S:.2f}')

# O valor inicial da variável S é zero
# O laço for vai iterar de i = 1 até i = 100 (inclusive).
# A função range cria uma sequência de números de 1 a 100, e para cada valor de i, a operação dentro do laço será realizada.
# Dentro do laço, a expressão 1 / i calcula o inverso de i.
# Esse valor é somado ao valor atual de S a cada iteração
# Por fim, o print irá imprimir o valor da soma S, formatado para 2 casas decimais.