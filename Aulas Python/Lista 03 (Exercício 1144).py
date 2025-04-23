# Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

# Saída
# Imprima a saída conforme o exemplo fornecido.

# Entrada               Saída
# 5                     1 1 1
#                       1 2 2
#                       2 4 8
#                       2 5 9
#                       3 9 27
#                       3 10 28
#                       4 16 64
#                       4 17 65
#                       5 25 125
#                       5 26 126

N = int(input())
for i in range(1, N + 1):
    quadrado = i * i
    cubo = i * i * i
    print(f'{i} {quadrado} {cubo}')
    print(f'{i} {quadrado + 1} {cubo + 1}')

# N é o valor de entrada inserido pelo usuário
# O laço for irá iterar de 1 até N (inclusive), ou seja, ele vai rodar N vezes.
# Em cada iteração, a variável i terá um valor entre 1 e N.
# A variável quadrado irá calcular o quadrado do valor i
# A variável cubo irá calcular o cubo do valor i
# A primeira linha impressa exibe o valor de i, seu quadrado e seu cubo, separados por espaços
# A segunda linha impressa exibe o valor de i, seu quadrado + 1 e seu cubo + 1, separados por espaços