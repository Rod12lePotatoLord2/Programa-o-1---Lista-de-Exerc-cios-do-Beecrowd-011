# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.
#
# Entrada
# A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).
#
# Saída
# Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho T justificados à direita e separados por espaço, onde T é igual ao número de dígitos do maior número da matriz. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.
#
# Exemplo de Entrada	Exemplo de Saída
# 1                            1
#
# 2                            1   2
#                              2   4
#
# 3                            1   2   4
#                              2   4   8
#                              4   8   16
#
# 4                            1   2   4   8
#                              2   4   8   16
#                              4   8   16  32
#                              8   16  32  64
#
# 5                            1   2   4   8   16
#                              2   4   8   16  32
#                              4   8   16  32  64
#                              8   16  32  64  128
#                              16  32  64  128 256
#
# 0

# Essa função constrói uma matriz de tamanho order x order. Cada elemento na posição [i][j] da matriz é calculado como 2^(i + j).
def construir(order):
    matriz = [[2 ** (i + j) for j in range(order)] for i in range(order)]
    return matriz

# Essa função imprime a matriz com alinhamento à direita.
def print_matriz(matriz):
    if not matriz:
        return
    valor_max = matriz[-1][-1]  # Maior número da matriz (último elemento, no canto inferior direito)
    largura_max = len(str(valor_max))  # Determina o espaço reservado para alinhar os números
    for fileira in matriz:
        print(' '.join(f'{valor:>{largura_max}}' for valor in fileira)) # Garante que todos os números fiquem alinhados corretamente em colunas

# Lê inteiros do usuário.
def main():
    while True:
        try:
            n = int(input())
            if n == 0:
                break   # Se n == 0, o programa encerra.
            if 0 <= n <= 15:
                matriz = construir(n)
                print_matriz(matriz)
                print()  # Se 0 <= n <= 15, constrói e imprime a matriz correspondente.
        except ValueError:
            break    # Em caso de error (valor não númerico), o loop termina.

# Garante que main() só será executada se o arquivo for executado diretamente, e não quando importado como módulo.
if __name__ == '__main__':
    main()