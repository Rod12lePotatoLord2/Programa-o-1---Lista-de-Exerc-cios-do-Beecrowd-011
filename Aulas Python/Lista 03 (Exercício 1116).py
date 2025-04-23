# Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

# Entrada
# A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

# Saída
# Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

# Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    if Y == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(X / Y))

# N é o valor de entrada inserido pelo usuário
# O laço for vai iterar N vezes.
# O _ é uma convenção usada quando o índice da iteração não é necessário.
# Dentro do laço for, o programa lê dois números inteiros, X e Y, que são inseridos pelo usuário.
# A função input() lê uma linha de entrada do usuário, split() separa essa linha por espaços e map(int, ...) converte as partes da entrada em números inteiros
# A condição if vai verificar se o valor armazenado em Y é 0.
# Se a condição for verdadeira, a mensagem 'divisao impossivel' será impressa na tela
# Caso contrário o programa calcula a divisão de X por Y (X / Y) e imprime o resultado formatado para ter uma casa decimal.
# A formatação :.1f garante que o resultado seja impresso com uma casa decimal.