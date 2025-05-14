# Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura) que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo.
#
# Obs: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A linha e a coluna começam em zero (0).
#
# Entrada
# A entrada contém vários casos de teste e termina com EOF (fim de arquivo. Cada caso de teste consiste de um valor inteiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz.
#
# Saída
# Para cada caso de teste, imprima a matriz correspondente conforme o exemplo abaixo. Após cada caso de teste, imprima uma linha em branco.
#
# Exemplo de Entrada	Exemplo de Saída
# 5                         20003
#                           01110
#                           01410
#                           01110
#                           30002
#
# 11                      20000000003
#                         02000000030
#                         00200000300
#                         00011111000
#                         00011111000
#                         00011411000
#                         00011111000
#                         00011111000
#                         00300000200
#                         03000000020
#                         30000000002

def preencher_matriz(N):
    matriz = [[0 for _ in range(N)] for _ in range(N)]

    # Diagonal principal = 2
    for i in range(N):
        matriz[i][i] = 2

    # Diagonal secundária = 3
    for i in range(N):
        matriz[i][N - 1 - i] = 3

    # Quadrado interno de 1s
    inicio = N // 3
    fim = N - inicio
    for i in range(inicio, fim):
        for j in range(inicio, fim):
            matriz[i][j] = 1

    # Centro = 4
    centro = N // 2
    matriz[centro][centro] = 4

    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(''.join(str(valor) for valor in linha))
    print()  # Linha em branco entre matrizes

try:
    while True:
        entrada = input()
        if entrada.strip() == '':
            continue
        N = int(entrada)
        matriz = preencher_matriz(N)
        imprimir_matriz(matriz)
except EOFError:
    pass

# Cria uma matriz N x N preenchida com 0s.
# Preenche a diagonal principal com 2s.
# Preenche a diagonal secundária com 3s.
# Calcula o quadrado interno com base em N // 3 e preenche com 1s.
# Substitui o ponto central da matriz com 4.
# Após cada matriz, imprime uma linha em branco.