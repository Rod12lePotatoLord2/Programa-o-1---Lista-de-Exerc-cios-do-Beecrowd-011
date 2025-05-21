# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.
#
# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).
#
# Saída
# Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.
#
# Exemplo de Entrada            Saída
# 5                             0 1 1 2 3

n = int(input()) # Entrada que lê um número inserido pelo usuário, transforma em inteiro e armazena na variável n

fibonacci = [] # Lista para armazenar os números da sequência

for i in range(n): # Geração da sequência
    if i == 0: # O primeiro termo é zero
        fibonacci.append(0)
    elif i == 1: # O segundo termo é um
        fibonacci.append(1)
    else: # O resto é a soma dos dois anteriores
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print(' '.join(map(str, fibonacci))) # Números são convertidos pra string, unidos com espaço, sem espaço no final.
# Impressão dos números na mesma linha, separados por espaço.
