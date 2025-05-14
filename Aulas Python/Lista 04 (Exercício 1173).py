# Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.
# 
# Entrada
# A entrada contém um valor inteiro (V<=50).
# 
# Saída
# Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o valor de V.
# 
# Exemplo de Entrada	Exemplo de Saída
# 1                       N[0] = 1
#                         N[1] = 2
#                         N[2] = 4
#                           ...

V = int(input()) # Lê um número inteiro da entrada e armazena em V
N = [0] * 10     # Cria a lista N com 10 posições, todas inicialmente com o valor 0:

N[0] = V         # O primeiro elemento da lista recebe o valor lido.
for i in range(1, 10):
    N[i] = N[i - 1] * 2 # A partir do segundo elemento (N[1]), cada valor é o dobro do anterior.

for i in range(10):
    print(f'N[{i}] = {N[i]}') # Imprime os valores da lista com seus respectivos índices