# Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

# Entrada
# O arquivo de entrada contém 1 valor inteiro qualquer.

# Saída
# Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

X = int(input())
for i in range(1, X+1):
    if i % 2 != 0:
        print(i)

# X é uma variável que armazenará um valor inteiro inserido pelo usuário
# O comando range(1, X+1) gera uma sequência de números que começa de 1 e vai até X (X incluso)
# O for i in range(1, X+1) faz o laço de repetição, onde i será o número atual da sequência gerada a cada iteração
# % é o módulo que calcula o resto da divisão de i por 2
# if i % 2 != 0, isso significa que i não é divisível por 2, ou seja, i é um número ímpar.
# Caso a condição seja verdadeira, o número é impresso na tela com print(i)