# Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.
# 
# Entrada
# A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.
# 
# Saída
# Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
# 
# Exemplo de Entrada	Exemplo de Saída
# 0                        X[0] = 1
# -5                       X[1] = 1
# 63                       X[2] = 63
# 0                        X[3] = 1
# ...                      ...

X = [int(input()) for _ in range(10)] # Cria uma lista "X" com 10 números inteiros. O input serão os valores inseridos pelo usuário. Int os converterá para inteiros e o for no range 10 repetirá isso 10x

X = [1 if valor <= 0 else valor for valor in X] # Usei compreensão de listas com uma expressão condicional. Para cada elemento de X, se for <= 0 será substituido por 1. Caso contrário o valor se mantém.

for i, valor in enumerate(X):
    print(f'X[{i}] = {valor}')

# Por fim, o código imprime cada valor da lista com seu índice no formato solicitado