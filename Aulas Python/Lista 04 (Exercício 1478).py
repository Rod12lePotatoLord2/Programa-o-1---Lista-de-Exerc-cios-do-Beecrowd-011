# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.
# 
# Entrada
# A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).
# 
# Saída
# Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. (os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.
#
# Exemplo de Entrada	Exemplo de Saída
# 1                            1
#
# 2                            1   2
#                              2   1
#
# 3                            1   2   3
#                              2   1   2
#                              3   2   1
#
# 4                            1   2   3   4
#                              2   1   2   3
#                              3   2   1   2
#                              4   3   2   1
#
# 5                            1   2   3   4   5
#                              2   1   2   3   4
#                              3   2   1   2   3
#                              4   3   2   1   2
#                              5   4   3   2   1
#
# 0

def construcao_de_matrizes():  # Define a função
    while True:   # Loop que lê um número N, se ele for = 0, o programa é interrompido
        N = int(input())
        if N == 0:
            break
        # Inicia a matriz com zeros
        matriz = [[0] * N for _ in range(N)] # Define cada elemento da matriz. A diagonal principal (quando i == j) recebe 1. A primeira vizinhança da diagonal recebe 2 (acima e abaixo da diagonal). A próxima recebe 3, e assim por diante.
        # Usa a fórmula 1 + abs(i - j) para preencher os valores.
        for i in range(N):
            for j in range(N):
                matriz[i][j] = 1 + abs(i - j)

        for fileira in matriz:
            print(' '.join(f'{num:3}' for num in fileira))
        print('')
# Cada linha (fileira) é impressa com os números alinhados à direita em 3 espaços, garantindo boa formatação visual. A linha em branco ao final separa a saída de diferentes matrizes.

construcao_de_matrizes()