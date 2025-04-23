# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.
 
# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

# Saída
# Imprima a soma de todos valores ímpares entre X e Y.

N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    if X > Y:
        X, Y = Y, X
    soma_impar = sum(i for i in range(X + 1, Y) if i % 2 != 0)
    print(soma_impar)

# N lerá um valor inteiro que indica quantos pares de números serão inseridos pelo usuário
# O for irá executar o bloco de código N vezes.
# O _ é usado quando a variável de controle do loop não será usada
# Os 2 valores inteiros inseridos, separados por espaço, serão armazenados nas variáveis X e Y
# A condicional if irá garantir que X seja sempre o menor e Y o maior valor entre os dois.
# Isso facilita ao calcular a soma dos números entre eles.
# A varíavel soma_impar irá gerar todos os números entre X e Y (excluindo os próprios X e Y) então fará a soma apenas dos ímpares.
# Por fim, o print irá imprimir os dados de saída obtidos