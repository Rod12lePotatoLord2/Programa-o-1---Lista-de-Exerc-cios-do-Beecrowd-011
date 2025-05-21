# á muito tempo atrás, em uma galáxia muito, muito distante...
#
# Após o declínio do Império, sucateiros estão espalhados por todo o universo procurando por um sabre de luz perdido. Todos sabem que um sabre de luz emite um padrão de ondas específico: 42 cercado por 7 em toda a volta. Você tem um sensor de ondas que varre um terreno com N x M células.
#
# Você deve escrever um programa que, dado um terreno N x M, procura pelo padrão do sabre de luz nele. Nenhuma varredura tem mais do que um padrão de sabre de luz.
#
# Entrada
# A primeira linha da entrada tem dois números positivos N e M, representando, respectivamente, o número de linhas e de colunas varridos no terreno (3 ≤ N, M ≤ 1000). Cada uma das próximas N linhas tem M inteiros, que descrevem os valores lidos em cada célula do terreno (-100 ≤ Tij ≤ 100, para 1 ≤ i ≤ N e 1 ≤ j ≤ M).
#
# Saída
# A saída é uma única linha com 2 inteiros X e Y separados por um espaço. Eles representam a coordenada (X,Y) do sabre de luz, caso encontrado. Se o terreno não tem um padrão de sabre de luz, X e Y são ambos zero.
#
# Exemplos de Entrada	Exemplos de Saída
# 4 7                         2 4
# 11 12 7 7 7 13 14
# 15 6 7 42 7 7 42
# 98 -5 7 7 7 42 7
# -1 42 3 9 7 7 7
#
# 4 7                         0 0
# 11 12 7 7 7 13 14
# 15 6 7 12 7 7 42
# 98 -5 7 7 7 42 7
# -1 42 3 9 7 7 7
#
# 3 3                         2 2
# 7 7 7
# 7 42 7
# 7 7 7

N, M = map(int, input().split()) # Lê o número de linhas (N) e colunas (M)
terreno = [] # Inicia a matriz (lista de listas)

for _ in range(N): # Para cada linha da matriz, o programa lê uma sequência de inteiros, transforma em lista e adiciona à matriz terreno.
    linha = list(map(int, input().split()))
    terreno.append(linha)
# Verifica cada célula que pode ser o centro do padrão
for i in range(1, N - 1): # Percorre linhas, ignorando as bordas
    for j in range(1, M - 1): # Percorre colunas, ignorando as bordas
        if terreno[i][j] == 42: # Verifica se a célula central tem o valor 42
            # Verifica se todas as 8 posições ao redor são 7
            if (terreno[i - 1][j - 1] == 7 and
                terreno[i - 1][j] == 7 and
                terreno[i - 1][j + 1] == 7 and
                terreno[i][j - 1] == 7 and
                terreno[i][j + 1] == 7 and
                terreno[i + 1][j - 1] == 7 and
                terreno[i + 1][j] == 7 and
                terreno[i + 1][j + 1] == 7):
                # Encontrado! Coordenadas devem ser 1-indexadas
                print(i + 1, j + 1)
                exit()

# Se chegou aqui, não encontrou
print(0, 0)
