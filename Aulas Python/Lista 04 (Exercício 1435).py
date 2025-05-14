# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.
#
# Entrada
# A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).
#
# Saída
# Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.
#
# Exemplo de Entrada	Exemplo de Saída
# 1                          1
# 2                          1   1
#                            1   1
#
# 3                          1   1   1
#                            1   2   1
#                            1   1   1
#
# 4                          1   1   1   1
#                            1   2   2   1
#                            1   2   2   1
#                            1   1   1   1
#
# 5                          1   1   1   1   1
#                            1   2   2   2   1
#                            1   2   3   2   1
#                            1   2   2   2   1
#                            1   1   1   1   1
#
# 0

while True:
    # Lê o valor de entrada
    N = int(input())
    if N == 0:
        break

    # Cria e popula a matriz
    matriz = [[min(i, j, N - i - 1, N - j - 1) + 1 for j in range(N)] for i in range(N)]

    # Imprime a matriz na formatação solicitada
    for fileira in matriz:
        print(' '.join(f'{val:3}' for val in fileira))
    print()