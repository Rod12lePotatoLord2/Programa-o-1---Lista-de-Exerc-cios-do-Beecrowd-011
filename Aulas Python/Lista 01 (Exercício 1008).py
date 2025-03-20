# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

# Entrada
# O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

# Saída
# Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

n = int(input()) # n é o valor inteiro que corresponde ao número do funcionário
h = int(input()) # h é o valor inteiro que corresponde às horas trabalhadas
v = float(input()) # v é o valor flutuante que corresponde ao valor recebido pelo funcionário

s = v * h  # s é o produto entre v e h, representando o salário desse funcionário

print(f'NUMBER = {n}')  # Essa função irá imprimir o número do funcionário
print(f'SALARY = U$ {s:.2f}') # Essa função irá imprimir o salário do funcionário em dólar