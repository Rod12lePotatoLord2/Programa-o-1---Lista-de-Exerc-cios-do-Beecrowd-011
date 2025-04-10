# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).

# Saída
# Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

# Exemplo de Entrada	Exemplo de Saída
# 5                      # 0 1 1 2 3

N = int(input())

lista_de_fibonacci = [0] * N

for i in range(0, N):

    if i <= 1:
        lista_de_fibonacci[i] = i
    else:
        lista_de_fibonacci[i] = lista_de_fibonacci[i - 1] + lista_de_fibonacci[i - 2]

    if i == N - 1:
        print(f'{lista_de_fibonacci[i]}', end='\n')
    else:
        print(f'{lista_de_fibonacci[i]}', end=' ')

# N será um valor inteiro inserido pelo usuário (Determinando quantos números da sequência de Fibonacci serão gerados e impressos
# lista_fibonacci é uma lista com N elementos, todos partem de 0
# for será um laço que itera de i = 0 até i = N -1. Realizando N interações (Uma pra cada número da sequência)
# O look investigará 2 casos(condições) para calcular os números da sequência de fibonacci:
# Nesse primeiro if - Caso i seja = 0 ou 1: a sequência de Fibonacci começa com os valores 0 e 1, então o código atribui o valor de 𝑖 À posição correspondente na lista
# Caso o i seja maio do que 1, o valor de Fibonacci na posição 𝑖 será a soma dos dois números anteriores da sequência
# O código imprime cada número de Fibonacci da lista, mas com uma diferença dependendo se é o último número ou não
# Quando chegar ao último número da sequência (na posição 𝑖 = 𝑁 − 1), ele é impresso seguido de uma quebra de linha
# \n é uma quebra de linha
# Para os números que não são os últimos, eles são impressos com um espaço entre eles, usando end=' ' para não fazer uma quebra de linha após cada número